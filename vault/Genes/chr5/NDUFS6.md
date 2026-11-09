---
symbol: "NDUFS6"
type: "gene"
col: 6998
ensembl_id: "ENSG00000145494"
name: "NADH:ubiquinone oxidoreductase subunit S6"
location: "5p15.33"
module: 36
arm: "+"
pooled_cpm: 39.15
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 0
n_dd_up_clean: 3
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# NDUFS6

*NADH:ubiquinone oxidoreductase subunit S6* — 5p15.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.20× (z +12.6, q 1e-33, up in 39 of 44 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 1.40× (z +3.6, q 0.018, up in 26 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (J82 0.364×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PTPMT1]] (+0.68, fdr 7e-06), [[NDUFAF5]] (+0.63, fdr 7e-06), [[SNRNP40]] (+0.61, fdr 1e-05); moves opposite to [[SDCBP]] (-0.65, fdr 7e-06), [[MED29]] (-0.61, fdr 3e-05), [[GOLGB1]] (-0.56, fdr 2e-05).
> It sits in the **+** arm of [[Module 036]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 9 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6998.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **3.20×** | +12.6 | 1e-33 | 39/44 (NCI-H460, SW480, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **2.25×** | +8.4 | 1e-14 | 30/37 (NCI-H460, SW480, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **2.49×** | +8.0 | 4e-13 | 33/42 (SW480, PANC-1, …) | all doses, flat | composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.90×** | +6.7 | 4e-09 | 39/47 (RKO, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **1.78×** | +6.3 | 5e-08 | 39/47 (SW480, HOP62, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~38% of this change | **1.72×** | +5.6 | 2e-06 | 34/47 (SNU-423, LoVo, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **1.54×** | +4.7 | 2e-04 | 32/48 (SW480, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~59% of this change | **1.49×** | +4.3 | 0.001 | 27/46 (SW 900, LOX-IMVI, …) | inconsistent across doses | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.40×** | +3.6 | 0.018 | 26/47 (HOP62, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.40×** | +3.6 | 0.018 | 25/47 (SW480, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.66×** | +3.3 | 0.049 | 22/48 (NCI-H23, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **1.63×** | +3.2 | 0.071 | 20/48 (HOP62, PANC-1, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6998.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (J82 0.364×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[GSK1059615 (drug)]] 5 µM |  | 0.394× | -3.7 | 0.14 | 23/47 (A-427, AN3 CA, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.747× | -3.2 | 0.42 | 23/48 (AsPC-1, Panc 03.27, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, +0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6998. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 52.0 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.74× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[A549 (line)]] | wt | 28.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.76× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 24.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.78× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[NCI-H460 (line)]] | wt | 40.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.69× (z +12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[A-172 (line)]] | wt | 28.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.17× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[A498 (line)]] | wt | 29.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.74× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[COLO 205 (line)]] | alt | 30.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.17× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[HOP62 (line)]] | alt | 24.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.94× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[Hs 766T (line)]] | wt | 44.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.51× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[J82 (line)]] | alt | 53.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.364× (z -11.8) |
| [[LoVo (line)]] | wt | 48.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.20× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[LOX-IMVI (line)]] | wt | 27.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.21× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[NCI-H1792 (line)]] | alt | 29.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.51× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[PANC-1 (line)]] | alt | 52.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.74× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[SNU-423 (line)]] | alt | 19.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.32× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[A-427 (line)]] | wt | 98.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 49.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 63.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 46.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 25.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 29.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 30.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 29.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 53.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 35.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 68.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 49.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 85.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 45.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 63.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 41.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 47.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 42.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 51.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 41.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6998), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTPMT1]] | +0.68 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[NDUFAF5]] | +0.63 | +0.59 / +0.60 | both halves | 7e-06 | pathway: Aerobic respiration and respiratory electron transport; STRING 841 |
| [[SNRNP40]] | +0.61 | +0.63 / +0.57 | both halves | 1e-05 |  |
| [[NUP93]] | +0.61 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[CDK5RAP1]] | +0.60 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[AAGAB]] | +0.59 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[KPNA1]] | +0.59 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[TIMM23B]] | +0.58 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[PTGES2]] | +0.58 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[DUS1L]] | +0.57 | +0.45 / +0.64 | both halves | 3e-05 |  |
| [[LSM12]] | +0.57 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[NDUFS5]] | +0.57 | +0.58 / +0.50 | both halves | 1e-05 | same gene group; pathway: Aerobic respiration and respiratory electron transport; STRING 999 |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SDCBP]] | -0.65 | -0.68 / -0.61 | both halves | 7e-06 |  |
| [[MED29]] | -0.61 | -0.61 / -0.45 | both halves | 3e-05 |  |
| [[GOLGB1]] | -0.56 | -0.60 / -0.48 | both halves | 2e-05 |  |
| [[AFF4]] | -0.52 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[TENT5C]] | -0.52 | -0.60 / -0.39 | both halves | 6e-05 |  |
| [[BCL10]] | -0.51 | -0.55 / -0.43 | both halves | 3e-05 |  |
| [[NOTCH2NLB]] | -0.50 | -0.55 / -0.43 | both halves | 3e-05 |  |
| [[ZBTB41]] | -0.50 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[RP2]] | -0.50 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[ATG12]] | -0.50 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[SFR1]] | -0.50 | -0.56 / -0.33 | both halves | 1e-04 |  |
| [[C6orf62]] | -0.49 | -0.52 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.606). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (-10.8, -17.9); signed map (-44.0, -24.5). **Vector** length 65.1, 17.6% of its response variance represented; |z| ≥ 3 in 545 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.9 | +6.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | +2.7 | +6.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~61% of this change | +2.2 | +3.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.8 | +0.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.8 | -0.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +2.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | +1.6 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +1.4 | +2.1 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -3.6 | -2.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.5 | +1.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | +0.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | -1.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.8 | -2.6 |
|  | [[AZD-8055 (drug)]] 0.5 µM |  | -1.6 | -2.4 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.5 | -3.7 |
|  | [[Glycyrrhizic acid (drug)]] 5 µM |  | -1.5 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | NADH:ubiquinone oxidoreductase subunit S6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5p15.33 — chr5:1,801,407-1,816,048 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CI-13kA |
| Gene groups (HGNC) | NADH:ubiquinone oxidoreductase supernumerary subunits |
| Hallmark sets | OXIDATIVE_PHOSPHORYLATION |
| Reactome | 3 pathways, smallest: Complex I biogenesis; Respiratory electron transport; Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [O75380](https://www.uniprot.org/uniprotkb/O75380) (NADH dehydrogenase):

> Accessory subunit of the mitochondrial membrane respiratory chain NADH dehydrogenase (Complex I), that is believed not to be involved in catalysis. Complex I functions in the transfer of electrons from NADH to the respiratory chain. The immediate electron acceptor for the enzyme is believed to be ubiquinone.

**Summary**, from NCBI Gene [4726](https://www.ncbi.nlm.nih.gov/gene/4726):

> This gene encodes a subunit of the NADH:ubiquinone oxidoreductase (complex I), which is the first enzyme complex in the electron transport chain of mitochondria. This complex functions in the transfer of electrons from NADH to the respiratory chain. The subunit encoded by this gene is one of seven subunits in the iron-sulfur protein fraction. Mutations in this gene cause mitochondrial complex I deficiency, a disease that causes a wide variety of clinical disorders, including neonatal disease …

**Accessions** — [HGNC:7713](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7713) · Entrez [4726](https://www.ncbi.nlm.nih.gov/gene/4726) · UniProt [O75380](https://www.uniprot.org/uniprotkb/O75380) · Ensembl [ENSG00000145494](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000145494)

## Data

Gene col 6998: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6998); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6998, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6998]; `tensor/DDL_lfc|DDL_z.npy` [6998]; `embed/gene_vectors.npy` [6998]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6998 or target_col == 6998). Every well: [[NDUFS6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NDUFS6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
