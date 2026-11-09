---
symbol: "MPLKIP"
type: "gene"
col: 9634
ensembl_id: "ENSG00000168303"
name: "M-phase specific PLK1 interacting protein"
location: "7p14.1"
module: 11
arm: "+"
pooled_cpm: 19.73
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 0
n_dd_up_clean: 5
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# MPLKIP

*M-phase specific PLK1 interacting protein* — 7p14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.82× (z +8.1, q 4e-13, up in 41 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (SHP-77 0.123×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Pitavastatin (Calcium) (drug)]] 5 µM in 1 line (COLO 205 0.0594×; ⚠ cell-cycle shift, explains ~89% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (BT-474 0.130×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C14orf119]] (+0.75, fdr 7e-06), [[RPP25L]] (+0.74, fdr 7e-06), [[SCAND1]] (+0.72, fdr 2e-05); moves opposite to [[RTEL1]] (-0.64, fdr 1e-05), [[PABIR2]] (-0.63, fdr 1e-05), [[INTS1]] (-0.63, fdr 7e-06).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 8 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9634.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.82×** | +8.1 | 4e-13 | 41/47 (AsPC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.07×** | +6.3 | 1e-07 | 37/43 (A498, H4, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.40×** | +4.5 | 0.001 | 25/48 (A498, NCI-H2347, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.60×** | +4.5 | 0.001 | 32/48 (BT-474, H4, …) | two highest doses | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change | **1.58×** | +4.4 | 0.001 | 23/42 (A498, C32, …) | inconsistent across doses | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.60×** | +4.1 | 0.005 | 30/48 (HOP62, PANC-1, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.60×** | +4.0 | 0.005 | 28/47 (COLO 205, NCI-H1573, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.50×** | +3.9 | 0.008 | 29/48 (A-172, HEC-1-A, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~55% of this change | **1.49×** | +3.8 | 0.009 | 25/44 (KATO III, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.44×** | +3.5 | 0.029 | 24/47 (NCI-H1573, AsPC-1, …) | all doses, flat | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +3.4 | 0.033 | 20/47 (HOP62, A498, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.28×** | +3.4 | 0.037 | 21/48 (HOP62, MIA PaCa-2, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.38×** | +3.1 | 0.088 | 16/47 (NCI-H2030, PANC-1, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9634.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (SHP-77 0.123×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Pitavastatin (Calcium) (drug)]] 5 µM in 1 line (COLO 205 0.0594×; ⚠ cell-cycle shift, explains ~89% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (BT-474 0.130×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | 0.536× | -3.1 | 0.96 | 18/47 (NCI-H2030, PANC-1, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, +0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9634. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 24.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.130× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 15.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.28× (z +8.5) | — |
| [[COLO 205 (line)]] | alt | 11.4 | 0 | 1 (1 ⚠) | — | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.0594× (z -9.7) ⚠ cell-cycle shift, explains ~89% of this change |
| [[SHP-77 (line)]] | alt | 27.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.123× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 24.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 26.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.99 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 27.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 41.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 27.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.13 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.32 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 22.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 28.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9634), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C14orf119]] | +0.75 | +0.63 / +0.76 | both halves | 7e-06 |  |
| [[RPP25L]] | +0.74 | +0.72 / +0.77 | both halves | 7e-06 |  |
| [[SCAND1]] | +0.72 | +0.47 / +0.78 | both halves | 2e-05 |  |
| [[TMEM60]] | +0.70 | +0.61 / +0.75 | both halves | 7e-06 |  |
| [[MRPS31]] | +0.68 | +0.62 / +0.73 | both halves | 7e-06 |  |
| [[PPCS]] | +0.67 | +0.69 / +0.67 | both halves | 7e-06 |  |
| [[MRPL46]] | +0.66 | +0.58 / +0.72 | both halves | 7e-06 |  |
| [[UQCRFS1]] | +0.66 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[FDX2]] | +0.65 | +0.54 / +0.69 | both halves | 1e-05 |  |
| [[REST]] | +0.65 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[EID2]] | +0.64 | +0.67 / +0.68 | both halves | 7e-06 |  |
| [[NDUFA7]] | +0.64 | +0.35 / +0.77 | both halves | 1e-04 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RTEL1]] | -0.64 | -0.56 / -0.63 | both halves | 1e-05 |  |
| [[PABIR2]] | -0.63 | -0.53 / -0.65 | both halves | 1e-05 |  |
| [[INTS1]] | -0.63 | -0.66 / -0.59 | both halves | 7e-06 |  |
| [[TCF3]] | -0.63 | -0.70 / -0.54 | both halves | 1e-05 |  |
| [[POLD1]] | -0.60 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[CPSF1]] | -0.60 | -0.54 / -0.54 | both halves | 1e-05 |  |
| [[MAPK9]] | -0.60 | -0.33 / -0.64 | both halves | 1e-04 |  |
| [[SMG1P3]] | -0.60 | -0.46 / -0.71 | both halves | 3e-05 |  |
| [[CS]] | -0.60 | -0.37 / -0.59 | both halves | 9e-05 |  |
| [[ARHGAP4]] | -0.60 | -0.35 / -0.62 | both halves | 1e-04 |  |
| [[TBCD]] | -0.59 | -0.52 / -0.56 | both halves | 1e-05 |  |
| [[LENG8]] | -0.59 | -0.57 / -0.64 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers MPLKIP's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.4% of all compounds | 0.015 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.636). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-42.3, -11.2); signed map (2.4, -18.5). **Vector** length 58.9, 12.0% of its response variance represented; |z| ≥ 3 in 542 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +3.3 | +4.5 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +3.1 | +3.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | +2.8 | +4.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.6 | +8.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +2.2 | +3.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.8 | +2.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | +3.4 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.1 | +2.2 |
|  | [[Ixazomib (drug)]] 0.05 µM |  | +1.1 | +1.5 |
|  | [[Arbutin (drug)]] 5 µM |  | +1.1 | +2.6 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -4.8 | +0.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -4.5 | +0.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change | -4.3 | +4.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | +2.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | -0.9 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.6 | -2.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.2 | +0.2 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -1.0 | -2.8 |
|  | [[Glycyrrhizic acid (drug)]] 0.5 µM |  | -1.0 | -1.6 |
|  | [[Hydroxyurea (drug)]] 5 µM |  | -1.0 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | M-phase specific PLK1 interacting protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p14.1 — chr7:40,126,027-40,134,622 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ORF20, TTDN1; previously C7orf11 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TAP9](https://www.uniprot.org/uniprotkb/Q8TAP9) (M-phase-specific PLK1-interacting protein):

> May play a role in maintenance of cell cycle integrity by regulating mitosis or cytokinesis.

**Summary**, from NCBI Gene [136647](https://www.ncbi.nlm.nih.gov/gene/136647):

> The protein encoded by this gene localizes to the centrosome during mitosis and to the midbody during cytokinesis. The protein is phosphorylated by cyclin-dependent kinase 1 during mitosis and subsequently interacts with polo-like kinase 1. The protein is thought to function in regulating mitosis and cytokinesis. Mutations in this gene result in nonphotosensitive trichothiodystrophy. [provided by RefSeq, Nov 2009]

**Accessions** — [HGNC:16002](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16002) · Entrez [136647](https://www.ncbi.nlm.nih.gov/gene/136647) · UniProt [Q8TAP9](https://www.uniprot.org/uniprotkb/Q8TAP9) · Ensembl [ENSG00000168303](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168303)

## Data

Gene col 9634: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9634); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9634, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9634]; `tensor/DDL_lfc|DDL_z.npy` [9634]; `embed/gene_vectors.npy` [9634]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9634 or target_col == 9634). Every well: [[MPLKIP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MPLKIP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
