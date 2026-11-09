---
symbol: "NLGN3"
type: "gene"
col: 12180
ensembl_id: "ENSG00000196338"
name: "neuroligin 3"
location: "Xq13.1"
module: 181
arm: "+"
pooled_cpm: 4.65
n_lines_expressing: 49
n_dd_up: 6
n_dd_down: 6
n_dd_up_clean: 5
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/181"]
generated_by: "tahoemap"
---

# NLGN3

*neuroligin 3* — Xq13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.70× (z +13.8, q 2e-40, up in 32 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.391× (z -9.3, q 1e-17, down in 31 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PILRA]] (+0.82, fdr 7e-06), [[C3orf20]] (+0.81, fdr 7e-06), [[MYOCOS]] (+0.79, fdr 7e-06); moves opposite to [[GCSH]] (-0.68, fdr 1e-05), [[SDHAF3]] (-0.67, fdr 1e-05).
> It is in [[Module 181]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[BTG3-AS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12180.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.70×** | +13.8 | 2e-40 | 32/38 (NCI-H460, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.89×** | +6.0 | 6e-07 | 3/6 (HOP62, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.81×** | +5.6 | 4e-06 | 20/44 (NCI-H460, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +5.4 | 1e-05 | 13/36 (PANC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.61×** | +4.7 | 4e-04 | 13/37 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Thymol (drug)]] 0.5 µM |  | **1.41×** | +3.3 | 0.076 | 7/30 (SW480, LoVo, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12180.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.391×** | -9.3 | 1e-17 | 31/45 (COLO 205, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.400×** | -9.0 | 4e-17 | 28/46 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.414×** | -8.7 | 6e-16 | 29/44 (SW480, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | **0.655×** | -4.0 | 0.008 | 13/28 (NCI-H1573, NCI-H23, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.784×** | -3.4 | 0.068 | 12/45 (SW480, Hs 766T, …) | top dose only | position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.530×** | -3.3 | 0.098 | 5/41 (COLO 205, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | 0.718× | -3.2 | 0.12 | 15/43 (NCI-H23, A-427, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~21% of this change | 0.733× | -3.1 | 0.14 | 12/46 (SW480, CHP-212, …) | all doses, stronger at high dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.32 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12180. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 11.6 | 0 | 2 | — | [[Hesperidin (drug)]] 5 µM 0.0916× (z -8.8) |
| [[SW480 (line)]] | alt | 7.55 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.224× (z -8.7) |
| [[A-427 (line)]] | wt | 5.11 | 0 | 1 | — | [[Ponatinib (drug)]] 0.5 µM 0.0753× (z -9.2) |
| [[AsPC-1 (line)]] | alt | 2.95 | 0 | 1 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0369× (z -9.5) ⚠ cell-cycle shift, explains ~33% of this change |
| [[COLO 205 (line)]] | alt | 10.5 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0326× (z -14.5) |
| [[HOP62 (line)]] | alt | 5.76 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.120× (z -9.0) ⚠ transcription drop; cell-cycle shift, explains ~57% of this change |
| [[NCI-H2030 (line)]] | alt | 3.59 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.38× (z +8.8) | — |
| [[NCI-H23 (line)]] | alt | 10.8 | 0 | 1 | — | [[Belumosudil (drug)]] 5 µM 0.0838× (z -11.6) |
| [[NCI-H460 (line)]] | wt | 6.99 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.80× (z +10.4) | — |
| [[PANC-1 (line)]] | alt | 1.79 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.47× (z +8.7) | — |
| [[SNU-423 (line)]] | alt | 3.95 | 0 | 1 | — | [[Lucanthone (drug)]] 0.5 µM 0.0615× (z -8.8) |
| [[A-172 (line)]] | wt | 5.11 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.90 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.08 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.68 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.53 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.80 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.12 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.59 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.65 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.59 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.85 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.42 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.52 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.38 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.81 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.48 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.77 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.26 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.29 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.41 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.02 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 5.37 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12180), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PILRA]] | +0.82 | +0.85 / +0.73 | both halves | 7e-06 |  |
| [[C3orf20]] | +0.81 | +0.77 / +0.79 | both halves | 7e-06 |  |
| [[MYOCOS]] | +0.79 | +0.78 / +0.72 | both halves | 7e-06 |  |
| [[GARIN1A]] | +0.79 | +0.74 / +0.73 | both halves | 7e-06 |  |
| [[COL11A2]] | +0.77 | +0.77 / +0.62 | both halves | 7e-06 |  |
| [[TGIF2-RAB5IF]] | +0.77 | +0.76 / +0.66 | both halves | 7e-06 |  |
| [[TMED6]] | +0.76 | +0.73 / +0.67 | both halves | 7e-06 |  |
| [[USP50]] | +0.76 | +0.76 / +0.64 | both halves | 7e-06 |  |
| [[FAM151B]] | +0.76 | +0.73 / +0.58 | both halves | 7e-06 |  |
| [[FNDC7]] | +0.75 | +0.79 / +0.66 | both halves | 7e-06 |  |
| [[LINC02936]] | +0.75 | +0.71 / +0.66 | both halves | 7e-06 |  |
| [[CCDC17]] | +0.75 | +0.68 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GCSH]] | -0.68 | -0.68 / -0.52 | both halves | 1e-05 |  |
| [[SDHAF3]] | -0.67 | -0.57 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BTG3-AS1]] | B | BTG3-AS1 activity raises NLGN3's level | lines that do not express BTG3-AS1 (7) vs lines expressing it (43) | 1.69× lower at baseline in the lines without BTG3-AS1 | 0.018 | ⚠ within organs, on part of the lines; also absent: DUSP8, USP43, EFNA2; maybe low, not absent |
| [[NFATC1]] | B | NFATC1 activity raises NLGN3's level | lines that do not express NFATC1 (11) vs lines expressing it (39) | 1.57× lower at baseline in the lines without NFATC1 | 0.028 | ⚠ within organs, on part of the lines; also absent: RIMKLB, HOMER2, RASGEF1C |
| [[WNK4]] | B | WNK4 activity raises NLGN3's level | lines that do not express WNK4 (5) vs lines expressing it (45) | 1.87× lower at baseline in the lines without WNK4 | 0.065 | ⚠ within organs, on part of the lines; also absent: TEX14, TMEM144, NEO1; maybe low, not absent |
| [[XG]] | B | XG activity raises NLGN3's level | lines that do not express XG (5) vs lines expressing it (45) | 1.66× lower at baseline in the lines without XG | 0.069 | ⚠ within organs, on part of the lines; also absent: TXNRD3, FSCN1, ELK3; maybe low, not absent |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises NLGN3's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises NLGN3's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[MMP25]] | C | MMP25 activity raises NLGN3's level | lines that do not express MMP25 (3) vs lines expressing it (47) | 1.53× lower at baseline in the lines without MMP25 | 0.088 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ENSG00000250842, MPP4, KDELR3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 181]]; 22 genes; every member is in the + arm (projection on the module's main direction 0.865). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (30.4, -13.7); signed map (18.3, 5.2). **Vector** length 79.8, 14.3% of its response variance represented; |z| ≥ 3 in 1,062 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +7.6 | +13.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.6 | +5.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.1 | +6.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.0 | +5.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.9 | +4.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.7 | +2.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | +2.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.2 | +0.6 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | +1.9 | +2.1 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.6 | +3.3 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -4.7 | -8.7 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.5 | -9.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.7 | -9.0 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.9 | -2.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.6 | -3.3 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -2.5 | -2.1 |
|  | [[Bexarotene (drug)]] 5 µM |  | -2.3 | -1.5 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -2.3 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | neuroligin 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq13.1 — chrX:71,144,821-71,175,255 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HNL3, KIAA1480, ASPGX1, AUTSX1 |
| Gene groups (HGNC) | Neuroligins |
| Hallmark sets | APICAL_JUNCTION |
| Reactome | 3 pathways, smallest: Neurexins and neuroligins; Protein-protein interactions at synapses; Neuronal System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NZ94](https://www.uniprot.org/uniprotkb/Q9NZ94) (Neuroligin-3):

> Cell surface protein involved in cell-cell-interactions via its interactions with neurexin family members. Plays a role in synapse function and synaptic signal transmission, and may mediate its effects by clustering other synaptic proteins. May promote the initial formation of synapses, but is not essential for this. May also play a role in glia-glia or glia-neuron interactions in the developing peripheral nervous system (By similarity).

**Summary**, from NCBI Gene [54413](https://www.ncbi.nlm.nih.gov/gene/54413):

> This gene encodes a member of a family of neuronal cell surface proteins. Members of this family may act as splice site-specific ligands for beta-neurexins and may be involved in the formation and remodeling of central nervous system synapses. Mutations in this gene may be associated with autism and Asperger syndrome. Multiple transcript variants encoding distinct isoforms have been identified for this gene. [provided by RefSeq, Oct 2009]

**Accessions** — [HGNC:14289](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14289) · Entrez [54413](https://www.ncbi.nlm.nih.gov/gene/54413) · UniProt [Q9NZ94](https://www.uniprot.org/uniprotkb/Q9NZ94) · Ensembl [ENSG00000196338](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196338)

## Data

Gene col 12180: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12180); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12180, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12180]; `tensor/DDL_lfc|DDL_z.npy` [12180]; `embed/gene_vectors.npy` [12180]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12180 or target_col == 12180). Every well: [[NLGN3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NLGN3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
