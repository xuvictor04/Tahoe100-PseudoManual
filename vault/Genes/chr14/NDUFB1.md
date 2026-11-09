---
symbol: "NDUFB1"
type: "gene"
col: 11429
ensembl_id: "ENSG00000183648"
name: "NADH:ubiquinone oxidoreductase subunit B1"
location: "14q31.3"
module: 48
arm: "+"
pooled_cpm: 25.43
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 0
n_dd_up_clean: 2
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/048"]
generated_by: "tahoemap"
---

# NDUFB1

*NADH:ubiquinone oxidoreductase subunit B1* — 14q31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.97× (z +8.8, q 1e-15, up in 38 of 41 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.93× (z +6.4, q 2e-08, up in 39 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (PANC-1 5.39×, NCI-H460 5.31×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (CFPAC-1 3.15×).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (Panc 03.27 0.287×, SK-MEL-2 0.245×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 14 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SMIM27]] (+0.75, fdr 7e-06), [[NDUFB11]] (+0.75, fdr 7e-06, ⚠ NDUFB11 in the vector space only through flagged drug-doses), [[NDUFC1]] (+0.74, fdr 8e-06), [[ROMO1]] (+0.74, fdr 7e-06); moves opposite to [[CCT2]] (-0.62, fdr 2e-05), [[HAPSTR1]] (-0.60, fdr 1e-05), [[PRELID3B]] (-0.59, fdr 3e-05).
> It sits in the **+** arm of [[Module 048]] (Aerobic respiration and respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 6 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11429.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (PANC-1 5.39×, NCI-H460 5.31×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (CFPAC-1 3.15×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **3.97×** | +8.8 | 1e-15 | 38/41 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **2.92×** | +6.7 | 8e-09 | 30/35 (NCI-H460, A549, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.93×** | +6.4 | 2e-08 | 39/47 (CFPAC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **2.21×** | +5.1 | 6e-05 | 31/38 (PANC-1, Hs 766T, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~35% of this change | **1.98×** | +4.7 | 3e-04 | 38/45 (AsPC-1, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.85×** | +3.8 | 0.014 | 33/43 (CFPAC-1, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.42×** | +3.4 | 0.052 | 31/48 (SNU-1, HOP62, …) | top dose only |  |
| [[Arbutin (drug)]] 5 µM |  | 1.67× | +3.2 | 0.11 | 26/47 (NCI-H2030, SW1417, …) | top dose only | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | 1.63× | +3.0 | 0.16 | 24/48 (HOP62, HEC-1-A, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11429.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (Panc 03.27 0.287×, SK-MEL-2 0.245×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | 0.693× | -3.6 | 0.15 | 27/47 (Panc 03.27, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.595× | -3.4 | 0.15 | 25/47 (SW480, SW1417, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | 0.360× | -3.4 | 0.15 | 27/46 (NCI-H23, SW480, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[GSK1059615 (drug)]] 5 µM |  | 0.394× | -3.1 | 0.31 | 30/46 (A-427, COLO 205, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.38 per unit of S-phase module lfc, +0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11429. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 27.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.15× (z +8.6) | — |
| [[NCI-H460 (line)]] | wt | 29.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.31× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[Panc 03.27 (line)]] | alt | 31.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -9.9) |
| [[PANC-1 (line)]] | alt | 23.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.39× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 17.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -9.1) |
| [[A-172 (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 36.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 26.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 24.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 35.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 68.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 27.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 28.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 24.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 25.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11429), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 14 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMIM27]] | +0.75 | +0.62 / +0.75 | both halves | 7e-06 |  |
| [[NDUFB11]] ⚠ | +0.75 | +0.59 / +0.84 | both halves | 7e-06 | same gene group; pathway: Aerobic respiration and respiratory electron transport; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[NDUFC1]] | +0.74 | +0.58 / +0.79 | both halves | 8e-06 | same gene group; pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 995 |
| [[ROMO1]] | +0.74 | +0.63 / +0.85 | both halves | 7e-06 |  |
| [[ATP5PD]] | +0.73 | +0.71 / +0.79 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 609 |
| [[C1orf122]] | +0.71 | +0.40 / +0.80 | both halves | 5e-05 |  |
| [[COX17]] | +0.71 | +0.59 / +0.81 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 723 |
| [[NDUFA1]] | +0.70 | +0.61 / +0.73 | both halves | 7e-06 | same gene group; pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 999 |
| [[COPS9]] | +0.70 | +0.58 / +0.76 | both halves | 8e-06 | STRING 468 |
| [[COX6B1]] | +0.70 | +0.55 / +0.80 | both halves | 1e-05 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 944 |
| [[UQCRQ]] ⚠ | +0.70 | +0.59 / +0.80 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 940; ⚠ in the vector space only through flagged drug-doses |
| [[SCAND1]] | +0.69 | +0.53 / +0.75 | both halves | 1e-05 |  |
| [[SNHG9]] | +0.69 | +0.56 / +0.78 | both halves | 1e-05 |  |
| [[DPM3]] | +0.67 | +0.57 / +0.73 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCT2]] | -0.62 | -0.48 / -0.60 | both halves | 2e-05 |  |
| [[HAPSTR1]] | -0.60 | -0.57 / -0.62 | both halves | 1e-05 |  |
| [[PRELID3B]] | -0.59 | -0.44 / -0.66 | both halves | 3e-05 |  |
| [[NRAS]] | -0.57 | -0.46 / -0.66 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 048]] — Aerobic respiration and respiratory electron transport; 93 genes; this gene is in the **+** arm (projection on the module's main direction 0.746). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-46.8, -21.3); signed map (-36.2, 9.4). **Vector** length 58.9, 17.0% of its response variance represented; |z| ≥ 3 in 470 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Complex IV assembly* (reactome, mean cos +0.59 to 11); *Formation of ATP by chemiosmotic coupling* (reactome, mean cos +0.63 to 7); *Cytoprotection by HMOX1* (reactome, mean cos +0.57 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.5 | +6.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.1 | +2.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +2.7 | +2.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.7 | +2.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.4 | +0.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +3.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.9 | -0.1 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.5 | +2.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.4 | +0.0 |
|  | [[Gemcitabine (drug)]] 0.5 µM |  | +1.2 | +1.4 |
| fall | [[Auranofin (drug)]] 5 µM |  | -3.5 | +0.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.8 | -2.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | -2.4 | +5.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | -1.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | -2.2 | +6.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.8 | +0.2 |
|  | [[EX229 (drug)]] 5 µM |  | -1.8 | -1.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.7 | -1.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.7 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | NADH:ubiquinone oxidoreductase subunit B1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q31.3 — chr14:92,116,122-92,121,917 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MNLL, CI-MNLL |
| Gene groups (HGNC) | NADH:ubiquinone oxidoreductase supernumerary subunits |
| Hallmark sets | OXIDATIVE_PHOSPHORYLATION |
| Reactome | 3 pathways, smallest: Complex I biogenesis; Respiratory electron transport; Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [O75438](https://www.uniprot.org/uniprotkb/O75438) (NADH dehydrogenase):

> Accessory subunit of the mitochondrial membrane respiratory chain NADH dehydrogenase (Complex I) that is believed not to be involved in catalysis. Complex I functions in the transfer of electrons from NADH to the respiratory chain. The immediate electron acceptor for the enzyme is believed to be ubiquinone.

**Summary**, from NCBI Gene [4707](https://www.ncbi.nlm.nih.gov/gene/4707):

> Predicted to enable NADH dehydrogenase (ubiquinone) activity. Predicted to be involved in mitochondrial electron transport, NADH to ubiquinone and proton motive force-driven mitochondrial ATP synthesis. Located in mitochondrial inner membrane. Part of respiratory chain complex I. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:7695](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7695) · Entrez [4707](https://www.ncbi.nlm.nih.gov/gene/4707) · UniProt [O75438](https://www.uniprot.org/uniprotkb/O75438) · Ensembl [ENSG00000183648](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183648)

## Data

Gene col 11429: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11429); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11429, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11429]; `tensor/DDL_lfc|DDL_z.npy` [11429]; `embed/gene_vectors.npy` [11429]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11429 or target_col == 11429). Every well: [[NDUFB1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NDUFB1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
