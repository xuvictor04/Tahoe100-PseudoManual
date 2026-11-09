---
symbol: "TMEM216"
type: "gene"
col: 11880
ensembl_id: "ENSG00000187049"
name: "transmembrane protein 216"
location: "11q13.1"
module: 12
arm: "+"
pooled_cpm: 4.39
n_lines_expressing: 44
n_dd_up: 3
n_dd_down: 5
n_dd_up_clean: 1
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 5
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# TMEM216

*transmembrane protein 216* — 11q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 1.57× (z +4.4, q 0.006, up in 13 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.508× (z -6.7, q 2e-08, down in 21 of 39 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RIOK2]] (+0.73, fdr 7e-06), [[DRG1]] (+0.73, fdr 7e-06), [[TARS2]] (+0.70, fdr 7e-06); moves opposite to [[RBBP7]] (-0.60, fdr 1e-05), [[APP]] (-0.59, fdr 1e-05), [[PGRMC1]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSMB5]] → it (grade B ⚠); 5 go from it, the strongest it → cells under [[5-Azacytidine (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11880.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.57×** | +4.4 | 0.006 | 13/34 (LS 180, SW480, …) | two highest doses | cell-cycle shift (explains ~19% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.32×** | +3.8 | 0.040 | 10/35 (NCI-H2030, LS 180, …) | two highest doses | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.48×** | +3.7 | 0.044 | 5/24 (KATO III, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Decitabine (drug)]] 0.5 µM |  | 1.36× | +3.0 | 0.27 | 3/34 (CFPAC-1, KATO III, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11880.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.508×** | -6.7 | 2e-08 | 21/39 (PANC-1, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.527×** | -6.3 | 9e-08 | 20/40 (NCI-H460, KATO III, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.613×** | -4.5 | 0.001 | 13/36 (Hs 766T, hTERT-HPNE, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.658×** | -4.1 | 0.005 | 14/37 (NCI-H2030, LS 180, …) | two highest doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.663×** | -3.9 | 0.011 | 15/34 (HOP62, RPMI-7951, …) | top dose only |  |
| [[Irinotecan (drug)]] 0.5 µM |  | 0.631× | -3.2 | 0.12 | 6/41 (NCI-H2347, COLO 205, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.731× | -3.1 | 0.14 | 12/37 (NCI-H2030, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | 0.722× | -3.1 | 0.14 | 12/30 (HS-578T, HOP62, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.35 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11880. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 2.09 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0549× (z -10.4) |
| [[RKO (line)]] | wt | 6.85 | 0 | 1 | — | [[Peretinoin (drug)]] 5 µM 0.0638× (z -10.5) |
| [[A-172 (line)]] | wt | 0.474 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.17 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.637 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 7.06 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.40 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.44 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.68 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.14 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.55 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.85 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.65 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.479 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 4.68 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.52 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.86 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.39 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.92 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.74 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.57 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.07 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.53 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.613 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 5.09 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.38 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.14 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.49 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.34 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.06 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.64 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.899 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.778 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.70 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.91 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.10 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 8.67 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11880), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RIOK2]] | +0.73 | +0.71 / +0.60 | both halves | 7e-06 |  |
| [[DRG1]] | +0.73 | +0.70 / +0.66 | both halves | 7e-06 |  |
| [[TARS2]] | +0.70 | +0.71 / +0.68 | both halves | 7e-06 |  |
| [[PSMD5]] | +0.70 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[RP9]] | +0.69 | +0.71 / +0.59 | both halves | 7e-06 |  |
| [[TRIM4]] | +0.67 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[ZNF230]] | +0.64 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[UFL1]] | +0.64 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[MTRES1]] | +0.63 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[TTI2]] | +0.63 | +0.53 / +0.69 | both halves | 1e-05 |  |
| [[MPHOSPH10]] | +0.63 | +0.57 / +0.65 | both halves | 1e-05 |  |
| [[SNHG11]] | +0.63 | +0.58 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBBP7]] | -0.60 | -0.56 / -0.58 | both halves | 1e-05 |  |
| [[APP]] | -0.59 | -0.63 / -0.54 | both halves | 1e-05 |  |
| [[PGRMC1]] | -0.58 | -0.54 / -0.54 | both halves | 1e-05 |  |
| [[MAPRE1]] | -0.58 | -0.41 / -0.65 | both halves | 4e-05 | pathway: Anchoring of the basal body to the plasma membrane |
| [[MOB1A]] | -0.57 | -0.49 / -0.60 | both halves | 1e-05 |  |
| [[YWHAQ]] | -0.57 | -0.50 / -0.63 | both halves | 1e-05 |  |
| [[SUMO3]] | -0.56 | -0.44 / -0.55 | both halves | 3e-05 |  |
| [[DYNC1H1]] | -0.56 | -0.49 / -0.63 | both halves | 1e-05 | pathway: Anchoring of the basal body to the plasma membrane |
| [[FUCA2]] | -0.56 | -0.52 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity raises TMEM216's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 0, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[5-Azacytidine (drug)]] 5 µM | C | TMEM216 activity raises the cells' numbers under 5-Azacytidine 5 µM (protects the cells) | lines that do not express TMEM216 (6) vs lines expressing it (42) | the lines without TMEM216: 0.74× the cells of the other lines | 0.023 | ⚠ tissue-confounded; across organs; also absent: H1-0, LPIN3, TACC2 |
| cells under [[Belinostat (drug)]] 5 µM | C | TMEM216 activity raises the cells' numbers under Belinostat 5 µM (protects the cells) | lines that do not express TMEM216 (6) vs lines expressing it (42) | the lines without TMEM216: 0.74× the cells of the other lines | 0.036 | ⚠ tissue-confounded; across organs; also absent: H1-0, LPIN3, TACC2 |
| cells under [[Doxorubicin (hydrochloride) (drug)]] 5 µM | C | TMEM216 activity raises the cells' numbers under Doxorubicin (hydrochloride) 5 µM (protects the cells) | lines that do not express TMEM216 (6) vs lines expressing it (42) | the lines without TMEM216: 0.55× the cells of the other lines | 0.082 | ⚠ tissue-confounded; across organs; also absent: H1-0, LPIN3, TACC2 |
| cells under [[Selinexor (drug)]] 0.5 µM | C | TMEM216 activity raises the cells' numbers under Selinexor 0.5 µM (protects the cells) | lines that do not express TMEM216 (6) vs lines expressing it (42) | the lines without TMEM216: 0.80× the cells of the other lines | 0.093 | ⚠ tissue-confounded; across organs; also absent: H1-0, LPIN3, TACC2 |
| cells under [[Panobinostat (drug)]] 5 µM | C | TMEM216 activity raises the cells' numbers under Panobinostat 5 µM (protects the cells) | lines that do not express TMEM216 (6) vs lines expressing it (42) | the lines without TMEM216: 0.70× the cells of the other lines | 0.097 | ⚠ tissue-confounded; across organs; also absent: H1-0, LPIN3, TACC2 |

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.677). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-37.1, -7.4); signed map (-13.3, -11.9). **Vector** length 53.6, 8.39% of its response variance represented; |z| ≥ 3 in 671 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +3.6 | +3.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.4 | +4.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.6 | +3.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +1.6 | +2.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +2.6 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.2 | +2.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.2 | -0.3 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | +1.1 | +2.2 |
|  | [[Pasireotide (acetate) (drug)]] 5 µM |  | +1.0 | +2.0 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.1 | -6.3 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.8 | -6.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.2 | -4.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -2.2 | -3.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.2 | -2.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.9 | -0.7 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.2 | -2.2 |
|  | [[Busulfan (drug)]] 5 µM |  | -1.1 | -0.8 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -1.1 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 216 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.1 — chr11:61,392,393-61,398,866 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC13379, HSPC244, JBTS2; previously CORS2, MKS2 |
| Reactome | 4 pathways, smallest: Anchoring of the basal body to the plasma membrane; Assembly of the 9+0 primary cilium; Cilium Assembly |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P0N5](https://www.uniprot.org/uniprotkb/Q9P0N5) (Transmembrane protein 216):

> Essential for primary ciliogenesis and embryonic development, facilitating the activation of Hedgehog (Hh) signaling pathway. Disrupts the interaction of GLI2 and GLI3 with the negative regulator SUFU. Inhibiting SUFU's interaction with GLI2 promotes the entry of GLI2 into the nucleus, allowing it to activate Hh target gene expression. Disrupting SUFU's interaction with GLI3 prevents its conversion into the repressor form, leading to increased nuclear GLI3 and enhanced Hh signaling. Required …

**Summary**, from NCBI Gene [51259](https://www.ncbi.nlm.nih.gov/gene/51259):

> This locus encodes a transmembrane domain-containing protein. Mutations at this locus have been associated with Meckel-Gruber Syndrome Type 2, and Joubert Syndrome 2, also known as Cerebello-oculorenal Syndrome 2. [provided by RefSeq, Aug 2010]

**Accessions** — [HGNC:25018](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25018) · Entrez [51259](https://www.ncbi.nlm.nih.gov/gene/51259) · UniProt [Q9P0N5](https://www.uniprot.org/uniprotkb/Q9P0N5) · Ensembl [ENSG00000187049](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000187049)

## Data

Gene col 11880: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11880); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11880, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11880]; `tensor/DDL_lfc|DDL_z.npy` [11880]; `embed/gene_vectors.npy` [11880]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11880 or target_col == 11880). Every well: [[TMEM216 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM216.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
