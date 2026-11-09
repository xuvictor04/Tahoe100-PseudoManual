---
symbol: "NDUFC1"
type: "gene"
col: 3048
ensembl_id: "ENSG00000109390"
name: "NADH:ubiquinone oxidoreductase subunit C1"
location: "4q31.1"
module: 24
arm: "+"
pooled_cpm: 38.86
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 2
n_dd_up_clean: 1
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# NDUFC1

*NADH:ubiquinone oxidoreductase subunit C1* — 4q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.30× (z +6.8, q 8e-09, up in 45 of 47 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.84× (z +5.4, q 2e-05, up in 44 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (AsPC-1 3.43×).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.508× (z -4.2, q 0.017, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SMIM27]] (+0.76, fdr 7e-06), [[TERF2IP]] (+0.76, fdr 7e-06), [[NDUFB1]] (+0.74, fdr 8e-06); moves opposite to [[ADAMTSL5]] (-0.71, fdr 7e-06), [[PRELID3B]] (-0.67, fdr 1e-05), [[CS]] (-0.66, fdr 8e-06).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 6 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3048.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (AsPC-1 3.43×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **3.30×** | +6.8 | 8e-09 | 45/47 (J82, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.84×** | +5.4 | 2e-05 | 44/48 (AsPC-1, HS-578T, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **2.42×** | +5.3 | 2e-05 | 36/39 (J82, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~51% of this change | **1.87×** | +3.9 | 0.014 | 38/47 (HOP62, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **1.92×** | +3.8 | 0.016 | 31/44 (J82, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.87×** | +3.8 | 0.016 | 36/47 (MIA PaCa-2, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | 1.70× | +3.2 | 0.11 | 31/48 (A-172, HS-578T, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change | 1.65× | +3.1 | 0.12 | 31/47 (NCI-H1573, COLO 205, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3048.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.508×** | -4.2 | 0.017 | 42/48 (C-33 A, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.537×** | -3.8 | 0.036 | 38/48 (LS 180, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | 0.585× | -3.3 | 0.17 | 35/48 (KATO III, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Sapanisertib (drug)]] 5 µM |  | 0.366× | -3.2 | 0.17 | 40/48 (HEC-1-A, A498, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, +0.64 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3048. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 24.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.43× (z +8.7) | — |
| [[A-172 (line)]] | wt | 39.7 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 56.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 38.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 30.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 52.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 67.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 44.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 46.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 34.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 45.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 49.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 59.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 40.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 28.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 26.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 42.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 51.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 34.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 52.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 55.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 59.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 51.9 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 35.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 63.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 55.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 47.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 43.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 23.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3048), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 7 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMIM27]] | +0.76 | +0.70 / +0.75 | both halves | 7e-06 |  |
| [[TERF2IP]] | +0.76 | +0.66 / +0.77 | both halves | 7e-06 |  |
| [[NDUFB1]] | +0.74 | +0.58 / +0.79 | both halves | 8e-06 | same gene group; pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 995 |
| [[NDUFA1]] | +0.73 | +0.66 / +0.81 | both halves | 7e-06 | same gene group; pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 998 |
| [[ARID4B]] | +0.71 | +0.54 / +0.71 | both halves | 1e-05 |  |
| [[ZNF821]] | +0.70 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[TMEM258]] | +0.70 | +0.59 / +0.81 | both halves | 7e-06 |  |
| [[COX6B1]] | +0.70 | +0.62 / +0.83 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 910 |
| [[COX17]] | +0.70 | +0.68 / +0.78 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION |
| [[SNHG9]] | +0.69 | +0.58 / +0.75 | both halves | 7e-06 |  |
| [[TRIM7-AS2]] | +0.69 | +0.62 / +0.76 | both halves | 7e-06 |  |
| [[NDUFA13]] ⚠ | +0.69 | +0.59 / +0.73 | both halves | 7e-06 | same gene group; pathway: Aerobic respiration and respiratory electron transport; STRING 997; ⚠ in the vector space only through flagged drug-doses |
| [[RBX1]] | +0.69 | +0.61 / +0.69 | both halves | 7e-06 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADAMTSL5]] | -0.71 | -0.60 / -0.65 | both halves | 7e-06 |  |
| [[PRELID3B]] | -0.67 | -0.56 / -0.67 | both halves | 1e-05 |  |
| [[CS]] | -0.66 | -0.58 / -0.61 | both halves | 8e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION |
| [[PSMG1]] | -0.64 | -0.49 / -0.60 | both halves | 1e-05 |  |
| [[MAPKAPK3]] | -0.64 | -0.55 / -0.60 | both halves | 1e-05 |  |
| [[STK25]] | -0.63 | -0.65 / -0.46 | both halves | 2e-05 |  |
| [[TTLL12]] | -0.63 | -0.60 / -0.48 | both halves | 2e-05 |  |
| [[EFTUD2]] | -0.62 | -0.50 / -0.66 | both halves | 1e-05 |  |
| [[CCT2]] | -0.62 | -0.48 / -0.62 | both halves | 2e-05 |  |
| [[SACS]] | -0.62 | -0.54 / -0.57 | both halves | 1e-05 |  |
| [[PRPF19]] | -0.62 | -0.46 / -0.64 | both halves | 2e-05 |  |
| [[ICMT]] | -0.62 | -0.54 / -0.60 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises NDUFC1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[C4orf47]] | C | C4orf47 activity raises NDUFC1's level | lines that do not express C4orf47 (3) vs lines expressing it (47) | 1.70× lower at baseline in the lines without C4orf47 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ENSG00000286162, CLEC2D, MPP4; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.607). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-39.4, -22.1); signed map (-6.6, 4.4). **Vector** length 67.0, 25.4% of its response variance represented; |z| ≥ 3 in 460 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.8 | +5.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.0 | +2.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.5 | +3.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +2.8 | -1.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +0.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.6 | +0.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.5 | -0.5 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.4 | +2.6 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.2 | +2.0 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | -4.3 | +3.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | -4.1 | +5.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.1 | -0.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | -3.9 | +6.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.7 | +1.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.9 | +0.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.2 | -1.1 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -1.1 | +1.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -1.1 | +1.5 |

## What is on record

|  |  |
|---|---|
| Name | NADH:ubiquinone oxidoreductase subunit C1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q31.1 — chr4:139,266,880-139,302,551 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KFYI |
| Gene groups (HGNC) | NADH:ubiquinone oxidoreductase supernumerary subunits |
| Hallmark sets | OXIDATIVE_PHOSPHORYLATION |
| Reactome | 3 pathways, smallest: Complex I biogenesis; Respiratory electron transport; Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [O43677](https://www.uniprot.org/uniprotkb/O43677) (NADH dehydrogenase):

> Accessory subunit of the mitochondrial membrane respiratory chain NADH dehydrogenase (Complex I), that is believed not to be involved in catalysis. Complex I functions in the transfer of electrons from NADH to the respiratory chain. The immediate electron acceptor for the enzyme is believed to be ubiquinone.

**Summary**, from NCBI Gene [4717](https://www.ncbi.nlm.nih.gov/gene/4717):

> The encoded protein is a subunit of the NADH:ubiquinone oxidoreductase (complex I), the first enzyme complex in the electron transport chain located in the inner mitochondrial membrane. Alternative splicing results in multiple transcript variants. [provided by RefSeq, May 2010]

**Accessions** — [HGNC:7705](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7705) · Entrez [4717](https://www.ncbi.nlm.nih.gov/gene/4717) · UniProt [O43677](https://www.uniprot.org/uniprotkb/O43677) · Ensembl [ENSG00000109390](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000109390)

## Data

Gene col 3048: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3048); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3048, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3048]; `tensor/DDL_lfc|DDL_z.npy` [3048]; `embed/gene_vectors.npy` [3048]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3048 or target_col == 3048). Every well: [[NDUFC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NDUFC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
