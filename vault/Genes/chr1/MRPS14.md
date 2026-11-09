---
symbol: "MRPS14"
type: "gene"
col: 4178
ensembl_id: "ENSG00000120333"
name: "mitochondrial ribosomal protein S14"
location: "1q25.1"
module: 220
arm: "+"
pooled_cpm: 11.95
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 0
n_dd_up_clean: 13
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/220"]
generated_by: "tahoemap"
---

# MRPS14

*mitochondrial ribosomal protein S14* — 1q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (15 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.59× (z +10.0, q 6e-21, up in 38 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (RKO 0.241×; ⚠ cell-cycle shift, would explain all of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (BT-474 0.182×; ⚠ toxic; cell-cycle shift, explains ~0% of this change); [[Cepharanthine (drug)]] 0.5 µM in 1 line (SW48 0.0740×); [[Drospirenone (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.0994×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NDUFA9]] (+0.63, fdr 2e-05), [[MRPL13]] (+0.60, fdr 1e-05), [[PEX2]] (+0.60, fdr 9e-06); moves opposite to [[PPIEL]] (-0.48, fdr 3e-05), [[FOSB]] (-0.47, fdr 3e-05), [[PPIEL-1]] (-0.43, fdr 9e-05).
> It is in [[Module 220]], a single-armed module (Respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 15 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4178.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **1.59×** | +10.0 | 6e-21 | 38/48 (NCI-H2347, A-427, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.89×** | +9.0 | 5e-17 | 20/31 (HT-29, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~20% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +7.9 | 6e-13 | 27/45 (SW480, PANC-1, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **1.61×** | +7.3 | 3e-11 | 28/36 (A-172, Panc 03.27, …) | all doses, flat | composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.59×** | +7.2 | 8e-11 | 27/47 (BT-474, A-172, …) | two highest doses | cell-cycle shift (explains ~22% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.45×** | +5.7 | 1e-06 | 20/47 (BT-474, LoVo, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **1.47×** | +5.7 | 1e-06 | 14/23 (NCI-H460, LOX-IMVI, …) | all doses, flat | composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.44×** | +5.4 | 4e-06 | 22/42 (NCI-H1573, A-427, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~32% of this change | **1.40×** | +5.1 | 2e-05 | 14/42 (HOP62, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[TAK-901 (drug)]] 5 µM |  | **1.98×** | +4.9 | 6e-05 | 19/47 (KATO III, LoVo, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.34×** | +4.5 | 4e-04 | 16/47 (A-172, BT-474, …) | two highest doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.47×** | +4.2 | 0.001 | 12/43 (HT-29, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.32×** | +4.1 | 0.002 | 11/46 (MIA PaCa-2, NCI-H23, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.30×** | +4.1 | 0.002 | 14/46 (Hs 766T, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.28×** | +3.8 | 0.006 | 11/47 (NCI-H1573, KATO III, …) | rises with dose | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.18× | +3.7 | 0.008 | 13/48 (NCI-H2030, SW480, …) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.39×** | +3.5 | 0.012 | 13/45 (SW480, C32, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.64×** | +3.5 | 0.012 | 14/43 (HEC-1-A, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.28×** | +3.5 | 0.012 | 13/45 (PANC-1, HEC-1-A, …) | all doses, flat | low cells (technical?) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.36×** | +3.3 | 0.023 | 7/44 (SHP-77, RKO, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.34×** | +3.2 | 0.032 | 9/45 (MIA PaCa-2, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **1.51×** | +3.0 | 0.065 | 2/41 (PANC-1, LS 180) | top dose only | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.21×** | +2.9 | 0.066 | 5/47 (SW 900, A-427, …) | top dose only |  |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (RKO 0.241×; ⚠ cell-cycle shift, would explain all of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (BT-474 0.182×; ⚠ toxic; cell-cycle shift, explains ~0% of this change); [[Cepharanthine (drug)]] 0.5 µM in 1 line (SW48 0.0740×); [[Drospirenone (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.0994×).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4178. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 17.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.182× (z -9.6) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 9.13 | 0 | 1 | — | [[Drospirenone (drug)]] 0.5 µM 0.0994× (z -8.9) |
| [[RKO (line)]] | wt | 15.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -11.9) ⚠ cell-cycle shift, would explain all of this change |
| [[SW48 (line)]] | wt | 9.27 | 0 | 1 | — | [[Cepharanthine (drug)]] 0.5 µM 0.0740× (z -9.2) |
| [[A-172 (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.42 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.31 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.26 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.83 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.97 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.12 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.52 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.97 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.20 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.82 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.69 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.25 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.51 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 16.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4178), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDUFA9]] | +0.63 | +0.69 / +0.48 | both halves | 2e-05 |  |
| [[MRPL13]] | +0.60 | +0.57 / +0.57 | both halves | 1e-05 | same gene group; pathway: Mitochondrial ribosome-associated quality control; STRING 998 |
| [[PEX2]] | +0.60 | +0.57 / +0.58 | both halves | 9e-06 |  |
| [[COA5]] | +0.60 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[TMEM69]] | +0.60 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[ZBTB26]] | +0.59 | +0.64 / +0.48 | both halves | 2e-05 |  |
| [[SNRNP35]] | +0.58 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[RAMAC]] | +0.56 | +0.46 / +0.57 | both halves | 3e-05 |  |
| [[NDUFS4]] | +0.55 | +0.46 / +0.65 | both halves | 2e-05 | STRING 683 |
| [[VPS16]] | +0.54 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[C1D]] | +0.54 | +0.53 / +0.40 | both halves | 5e-05 |  |
| [[C6orf89]] | +0.54 | +0.57 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPIEL]] | -0.48 | -0.43 / -0.52 | both halves | 3e-05 |  |
| [[FOSB]] | -0.47 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[PPIEL-1]] | -0.43 | -0.36 / -0.45 | both halves | 9e-05 |  |
| [[PABPC4]] | -0.43 | -0.34 / -0.38 | both halves | 1e-04 |  |
| [[PRKCG]] | -0.43 | -0.44 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 220]] — Respiratory electron transport; 11 genes; every member is in the + arm (projection on the module's main direction 0.731). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-41.6, 16.6); signed map (-11.6, -16.3). **Vector** length 56.0, 8.06% of its response variance represented; |z| ≥ 3 in 654 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Respiratory electron transport* (reactome, mean cos +0.58 to 4); *Complex I biogenesis* (reactome, mean cos +0.57 to 3); *Aerobic respiration and respiratory electron transport* (reactome, mean cos +0.58 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +7.0 | +10.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.0 | +4.9 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +3.6 | +4.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | +3.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.2 | +3.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.6 | +3.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.6 | +4.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.5 | +2.8 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | -2.0 | -0.5 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.4 | -2.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.4 | -0.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.2 | -1.9 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -1.2 | -0.8 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.2 | -0.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.1 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial ribosomal protein S14 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q25.1 — chr1:175,010,789-175,023,425 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HSMRPS14, uS14m |
| Gene groups (HGNC) | Mitochondrial ribosomal proteins; Small subunit mitochondrial ribosomal proteins |
| Reactome | 6 pathways, smallest: Mitochondrial ribosome-associated quality control; Mitochondrial translation elongation; Mitochondrial translation initiation |
| Matched by | ensembl_id |

UniProt [O60783](https://www.uniprot.org/uniprotkb/O60783) carries no function annotation.

**Summary**, from NCBI Gene [63931](https://www.ncbi.nlm.nih.gov/gene/63931):

> Mammalian mitochondrial ribosomal proteins are encoded by nuclear genes and help in protein synthesis within the mitochondrion. Mitochondrial ribosomes (mitoribosomes) consist of a small 28S subunit and a large 39S subunit. They have an estimated 75% protein to rRNA composition compared to prokaryotic ribosomes, where this ratio is reversed. Another difference between mammalian mitoribosomes and prokaryotic ribosomes is that the latter contain a 5S rRNA. Among different species, the proteins …

**Accessions** — [HGNC:14049](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14049) · Entrez [63931](https://www.ncbi.nlm.nih.gov/gene/63931) · UniProt [O60783](https://www.uniprot.org/uniprotkb/O60783) · Ensembl [ENSG00000120333](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000120333)

## Data

Gene col 4178: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4178); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4178, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4178]; `tensor/DDL_lfc|DDL_z.npy` [4178]; `embed/gene_vectors.npy` [4178]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4178 or target_col == 4178). Every well: [[MRPS14 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MRPS14.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
