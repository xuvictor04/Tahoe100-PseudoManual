---
symbol: "COX8A"
type: "gene"
col: 10704
ensembl_id: "ENSG00000176340"
name: "cytochrome c oxidase subunit 8A"
location: "11q13.1"
module: 48
arm: "+"
pooled_cpm: 54.29
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 0
n_dd_up_clean: 1
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/048"]
generated_by: "tahoemap"
---

# COX8A

*cytochrome c oxidase subunit 8A* — 11q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.39× (z +7.8, q 3e-12, up in 38 of 39 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change. The strongest without an alert is [[Arbutin (drug)]] 5 µM: 1.68× (z +3.3, q 0.073, up in 37 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H1573 7.67×, SW480 4.82×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 13 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UQCRQ]] (+0.73, fdr 7e-06, ⚠ UQCRQ in the vector space only through flagged drug-doses), [[MIF]] (+0.71, fdr 7e-06), [[NDUFA2]] (+0.71, fdr 1e-05), [[SSR4]] (+0.70, fdr 7e-06); moves opposite to [[SLC4A3]] (-0.61, fdr 1e-05), [[RIPOR1]] (-0.56, fdr 5e-05), [[DBN1]] (-0.55, fdr 9e-05).
> It sits in the **+** arm of [[Module 048]] (Aerobic respiration and respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 6 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10704.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H1573 7.67×, SW480 4.82×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **3.39×** | +7.8 | 3e-12 | 38/39 (NCI-H1573, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **4.21×** | +7.4 | 3e-11 | 46/47 (PANC-1, A-172, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~44% of this change | **2.27×** | +5.5 | 8e-06 | 45/47 (SW1417, SW 900, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **2.40×** | +5.4 | 1e-05 | 41/45 (KATO III, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.96×** | +4.3 | 0.002 | 38/47 (CFPAC-1, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change | **1.77×** | +3.8 | 0.014 | 38/47 (PANC-1, SW480, …) | top dose only | position effect removed |
| [[Arbutin (drug)]] 5 µM |  | **1.68×** | +3.3 | 0.073 | 37/48 (SW1417, A-172, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10704.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Sapanisertib (drug)]] 5 µM |  | 0.377× | -3.3 | 0.56 | 38/48 (LoVo, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | 0.401× | -3.1 | 0.56 | 35/48 (BT-474, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.32 per unit of S-phase module lfc, +0.66 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10704. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 35.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.67× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[SW480 (line)]] | alt | 58.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.82× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[A-172 (line)]] | wt | 49.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 89.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 37.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 47.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 55.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 52.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 44.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 42.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 59.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 37.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 48.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 43.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 50.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 30.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 66.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 53.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 67.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 42.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 59.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 111 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 48.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 39.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 71.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 75.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 74.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 34.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 48.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 61.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 61.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 69.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 56.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 48.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 62.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 40.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 43.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 48.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 69.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 68.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 44.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10704), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 12 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UQCRQ]] ⚠ | +0.73 | +0.62 / +0.79 | both halves | 7e-06 | pathway: HALLMARK_ADIPOGENESIS; STRING 824; ⚠ in the vector space only through flagged drug-doses |
| [[MIF]] | +0.71 | +0.64 / +0.75 | both halves | 7e-06 |  |
| [[NDUFA2]] | +0.71 | +0.57 / +0.75 | both halves | 1e-05 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 582 |
| [[SSR4]] | +0.70 | +0.60 / +0.73 | both halves | 7e-06 |  |
| [[NDUFB11]] ⚠ | +0.70 | +0.63 / +0.71 | both halves | 7e-06 | pathway: Aerobic respiration and respiratory electron transport; STRING 606; ⚠ in the vector space only through flagged drug-doses |
| [[ROMO1]] | +0.69 | +0.63 / +0.72 | both halves | 7e-06 | STRING 487 |
| [[OST4]] | +0.69 | +0.61 / +0.70 | both halves | 7e-06 |  |
| [[COX7A2]] ⚠ | +0.69 | +0.68 / +0.69 | both halves | 7e-06 | same gene group; pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 988; ⚠ in the vector space only through flagged drug-doses |
| [[COX7B]] | +0.68 | +0.62 / +0.65 | both halves | 7e-06 | same gene group; pathway: HALLMARK_ADIPOGENESIS; STRING 997 |
| [[DDT]] | +0.68 | +0.59 / +0.72 | both halves | 7e-06 | pathway: HALLMARK_ADIPOGENESIS |
| [[ANAPC11]] | +0.67 | +0.66 / +0.77 | both halves | 7e-06 |  |
| [[SPCS1]] | +0.66 | +0.47 / +0.73 | both halves | 2e-05 |  |
| [[ATP5F1E]] | +0.64 | +0.58 / +0.66 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 521 |
| [[DPM3]] | +0.64 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[COX6A1]] | +0.64 | +0.59 / +0.73 | both halves | 7e-06 | same gene group; pathway: HALLMARK_ADIPOGENESIS; STRING 998 |

## Genes that move opposite

*16 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC4A3]] | -0.61 | -0.51 / -0.64 | both halves | 1e-05 |  |
| [[RIPOR1]] | -0.56 | -0.40 / -0.57 | both halves | 5e-05 |  |
| [[DBN1]] | -0.55 | -0.36 / -0.63 | both halves | 9e-05 |  |
| [[ZNF783]] ⚠ | -0.54 | -0.51 / -0.42 | both halves | 4e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[NPEPL1]] | -0.54 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[PLEKHG4]] | -0.53 | -0.49 / -0.46 | both halves | 3e-05 |  |
| [[SLC35F6]] | -0.53 | -0.35 / -0.60 | both halves | 1e-04 |  |
| [[LZTR1]] | -0.52 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[SRP14-DT]] | -0.51 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[SFPQ]] | -0.51 | -0.38 / -0.53 | both halves | 7e-05 |  |
| [[NUDC]] | -0.51 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[CCT2]] | -0.51 | -0.39 / -0.52 | both halves | 6e-05 |  |
| [[ZNF300]] | -0.51 | -0.33 / -0.54 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 048]] — Aerobic respiration and respiratory electron transport; 93 genes; this gene is in the **+** arm (projection on the module's main direction 0.721). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-47.0, -22.2); signed map (-34.9, 10.5). **Vector** length 55.8, 19.9% of its response variance represented; |z| ≥ 3 in 487 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Formation of ATP by chemiosmotic coupling* (reactome, mean cos +0.59 to 7); *Cristae formation* (reactome, mean cos +0.59 to 7); *Mitochondrial biogenesis* (reactome, mean cos +0.59 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change | +2.4 | +3.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.3 | +0.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.0 | +1.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.7 | +0.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift | +1.4 | +1.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.1 | -1.5 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 5 µM |  | +1.0 | +1.2 |
|  | [[Arbutin (drug)]] 5 µM |  | +0.9 | +3.3 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | +0.9 | -0.9 |
|  | [[Almonertinib (hydrochloride) (drug)]] 0.05 µM |  | +0.9 | +0.2 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.3 | -0.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | -4.6 | +7.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | -4.2 | +7.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | -4.2 | +5.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.8 | +2.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.4 | +0.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.1 | +0.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.8 | +0.4 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -1.6 | +1.8 |

## What is on record

|  |  |
|---|---|
| Name | cytochrome c oxidase subunit 8A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.1 — chr11:63,974,620-63,976,543 (+) |
| Ensembl biotype | protein_coding |
| Also known as | COX8-2, COX8L, VIII-L, COX, VIII; previously COX8 |
| Gene groups (HGNC) | Mitochondrial complex IV: cytochrome c oxidase subunits |
| Hallmark sets | ADIPOGENESIS, OXIDATIVE_PHOSPHORYLATION |
| Reactome | 9 pathways, smallest: Complex IV assembly; Cytoprotection by HMOX1; TP53 Regulates Metabolic Genes |
| Matched by | ensembl_id |

**Function**, from UniProt [P10176](https://www.uniprot.org/uniprotkb/P10176) (Cytochrome c oxidase subunit 8A, mitochondrial):

> Component of the cytochrome c oxidase, the last enzyme in the mitochondrial electron transport chain which drives oxidative phosphorylation. The respiratory chain contains 3 multisubunit complexes succinate dehydrogenase (complex II, CII), ubiquinol-cytochrome c oxidoreductase (cytochrome b-c1 complex, complex III, CIII) and cytochrome c oxidase (complex IV, CIV), that cooperate to transfer electrons derived from NADH and succinate to molecular oxygen, creating an electrochemical gradient over …

**Summary**, from NCBI Gene [1351](https://www.ncbi.nlm.nih.gov/gene/1351):

> The protein encoded by this gene is the terminal enzyme of the respiratory chain, coupling the transfer of electrons from cytochrome c to molecular oxygen, with the concomitant production of a proton electrochemical gradient across the inner mitochondrial membrane. In addition to 3 mitochondrially encoded subunits, which perform the catalytic function, the eukaryotic enzyme contains nuclear-encoded smaller subunits, ranging in number from 4 in some organisms to 10 in mammals. It has been …

**Accessions** — [HGNC:2294](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2294) · Entrez [1351](https://www.ncbi.nlm.nih.gov/gene/1351) · UniProt [P10176](https://www.uniprot.org/uniprotkb/P10176) · Ensembl [ENSG00000176340](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000176340)

## Data

Gene col 10704: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10704); `tables/drug_effects.parquet` (9 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10704, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10704]; `tensor/DDL_lfc|DDL_z.npy` [10704]; `embed/gene_vectors.npy` [10704]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10704 or target_col == 10704). Every well: [[COX8A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COX8A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
