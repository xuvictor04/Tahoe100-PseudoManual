---
symbol: "NAA38"
type: "gene"
col: 11356
ensembl_id: "ENSG00000183011"
name: "N-alpha-acetyltransferase 38, NatC auxiliary subunit"
location: "17p13.1"
module: 24
arm: "+"
pooled_cpm: 27.93
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 1
n_dd_up_clean: 2
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# NAA38

*N-alpha-acetyltransferase 38, NatC auxiliary subunit* — 17p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.72× (z +7.6, q 2e-11, up in 40 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (PANC-1 2.44×, NCI-H23 2.49×).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[PH-797804 (drug)]] 5 µM: 0.408× (z -4.6, q 0.002, down in 33 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[TAK-901 (drug)]] 5 µM in 1 line (NCI-H23 0.0432×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (COLO 205 0.227×); [[Dinaciclib (drug)]] 5 µM in 1 line (SW480 0.323×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF821]] (+0.72, fdr 7e-06), [[SMIM27]] (+0.72, fdr 7e-06), [[PNISR]] (+0.68, fdr 7e-06); moves opposite to [[NOLC1]] (-0.67, fdr 1e-05), [[EIF4G1]] (-0.63, fdr 1e-05), [[BLTP2]] (-0.62, fdr 7e-06).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 7 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11356.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (PANC-1 2.44×, NCI-H23 2.49×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.72×** | +7.6 | 2e-11 | 40/47 (PANC-1, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.03×** | +7.0 | 8e-10 | 34/44 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.62×** | +4.5 | 0.001 | 24/37 (LS 180, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.60×** | +4.5 | 0.001 | 28/43 (SW 900, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.53×** | +4.2 | 0.004 | 23/46 (NCI-H2347, Panc 03.27, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~24% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.48×** | +3.8 | 0.012 | 32/47 (HCT15, PANC-1, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.46×** | +3.8 | 0.014 | 26/48 (A549, J82, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.58×** | +3.3 | 0.063 | 20/40 (LOX-IMVI, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **1.26×** | +3.2 | 0.090 | 23/47 (SNU-1, PANC-1, …) | top dose only | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | 1.39× | +3.1 | 0.11 | 21/47 (HT-29, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 1.36× | +3.0 | 0.12 | 17/48 (LOX-IMVI, HepG2/C3A, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11356.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[TAK-901 (drug)]] 5 µM in 1 line (NCI-H23 0.0432×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (COLO 205 0.227×); [[Dinaciclib (drug)]] 5 µM in 1 line (SW480 0.323×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **0.408×** | -4.6 | 0.002 | 33/48 (SNU-1, COLO 205, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | 0.500× | -3.6 | 0.10 | 23/49 (NCI-H23, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.715× | -3.3 | 0.18 | 22/48 (NCI-H460, Hs 766T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11356. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 30.8 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.49× (z +8.7) | [[TAK-901 (drug)]] 5 µM 0.0432× (z -11.1) |
| [[COLO 205 (line)]] | alt | 62.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.227× (z -10.1) |
| [[PANC-1 (line)]] | alt | 22.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.44× (z +8.8) | — |
| [[SW480 (line)]] | alt | 35.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.323× (z -9.4) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 30.2 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 38.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 39.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.90 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 28.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 20.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 49.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 61.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 32.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 23.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 43.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 25.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 36.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 35.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 47.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 25.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 35.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 21.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11356), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 5 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF821]] | +0.72 | +0.68 / +0.70 | both halves | 7e-06 |  |
| [[SMIM27]] | +0.72 | +0.62 / +0.73 | both halves | 7e-06 |  |
| [[PNISR]] | +0.68 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[NDUFC1]] | +0.67 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[NDUFA1]] | +0.66 | +0.55 / +0.70 | both halves | 1e-05 |  |
| [[C1orf56]] | +0.66 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[TERF2IP]] | +0.65 | +0.56 / +0.69 | both halves | 1e-05 |  |
| [[NDUFB1]] | +0.65 | +0.61 / +0.68 | both halves | 7e-06 |  |
| [[SNHG9]] | +0.65 | +0.54 / +0.75 | both halves | 1e-05 |  |
| [[HOXA-AS2]] | +0.64 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[PABPN1]] | +0.64 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[ZSCAN16-AS1]] | +0.64 | +0.63 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NOLC1]] | -0.67 | -0.54 / -0.70 | both halves | 1e-05 | pathway: HALLMARK_E2F_TARGETS |
| [[EIF4G1]] | -0.63 | -0.53 / -0.73 | both halves | 1e-05 |  |
| [[BLTP2]] | -0.62 | -0.64 / -0.58 | both halves | 7e-06 |  |
| [[IPO7]] | -0.62 | -0.57 / -0.60 | both halves | 1e-05 | pathway: HALLMARK_E2F_TARGETS |
| [[EIF2S1]] | -0.61 | -0.44 / -0.69 | both halves | 3e-05 | pathway: HALLMARK_E2F_TARGETS |
| [[PRKDC]] | -0.61 | -0.53 / -0.63 | both halves | 1e-05 | pathway: HALLMARK_E2F_TARGETS |
| [[PRELID3B]] | -0.60 | -0.49 / -0.63 | both halves | 1e-05 |  |
| [[PLXNA1]] | -0.59 | -0.60 / -0.54 | both halves | 1e-05 |  |
| [[RUVBL1]] | -0.59 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[TTLL12]] | -0.59 | -0.54 / -0.54 | both halves | 1e-05 |  |
| [[CCT2]] | -0.59 | -0.49 / -0.54 | both halves | 1e-05 |  |
| [[PSMG1]] | -0.58 | -0.42 / -0.51 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.575). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-39.9, -21.9); signed map (-6.3, 2.8). **Vector** length 76.4, 19.2% of its response variance represented; |z| ≥ 3 in 528 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.7 | +7.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.7 | +2.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | +4.3 | +3.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.4 | +0.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.2 | -0.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.7 | +1.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.1 | +2.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.1 | +0.4 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.0 | +2.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.0 | +2.0 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.2 | -3.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.5 | -0.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.3 | -1.1 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -2.2 | -1.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | -0.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.0 | -1.2 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.0 | -1.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.8 | -4.6 |

## What is on record

|  |  |
|---|---|
| Name | N-alpha-acetyltransferase 38, NatC auxiliary subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.1 — chr17:7,856,685-7,885,238 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC14151, PFAAP2; previously LSMD1 |
| Gene groups (HGNC) | N-alpha-acetyltransferase subunits; LSm proteins |
| Hallmark sets | E2F_TARGETS |
| Reactome | 4 pathways, smallest: Retrograde transport at the Trans-Golgi-Network; Intra-Golgi and retrograde Golgi-to-ER traffic; Membrane Trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BRA0](https://www.uniprot.org/uniprotkb/Q9BRA0) (N-alpha-acetyltransferase 38, NatC auxiliary subunit):

> Auxillary component of the N-terminal acetyltransferase C (NatC) complex which catalyzes acetylation of N-terminal methionine residues. N-terminal acetylation protects proteins from ubiquitination and degradation by the N-end rule pathway.

**Summary**, from NCBI Gene [84316](https://www.ncbi.nlm.nih.gov/gene/84316):

> Predicted to enable RNA binding activity. Involved in negative regulation of apoptotic process. Located in cytoplasm and nucleoplasm. Part of NatC complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28212](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28212) · Entrez [84316](https://www.ncbi.nlm.nih.gov/gene/84316) · UniProt [Q9BRA0](https://www.uniprot.org/uniprotkb/Q9BRA0) · Ensembl [ENSG00000183011](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183011)

## Data

Gene col 11356: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11356); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11356, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11356]; `tensor/DDL_lfc|DDL_z.npy` [11356]; `embed/gene_vectors.npy` [11356]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11356 or target_col == 11356). Every well: [[NAA38 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NAA38.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
