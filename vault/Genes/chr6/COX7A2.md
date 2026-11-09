---
symbol: "COX7A2"
type: "gene"
col: 3395
ensembl_id: "ENSG00000112695"
name: "cytochrome c oxidase subunit 7A2"
location: "6q14.1"
module: 48
arm: "+"
pooled_cpm: 65.52
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 0
n_dd_up_clean: 0
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/048", "evidence-flagged-only"]
generated_by: "tahoemap"
---

# COX7A2

*cytochrome c oxidase subunit 7A2* — 6q14.1

## At a glance

> [!summary] In this data
> ⚠ It is in the vector space only through drug-doses that carry an alert for it (its significant pooled drug-doses and per-line responses; `embed/genes.parquet` evidence_flagged_only): its vector, partners and module rest on changes that may come from what those drug-doses did to the cells rather than from its own regulation.
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.55× (z +6.6, q 3e-08, up in 46 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (A549 4.54×, SNU-1 6.68×, NCI-H1573 4.56×, PANC-1 3.92×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (H4 0.381×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 21 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NDUFA1]] (+0.84, fdr 7e-06), [[COX6B1]] (+0.82, fdr 7e-06), [[NDUFB11]] (+0.80, fdr 7e-06, ⚠ NDUFB11 in the vector space only through flagged drug-doses), [[NDUFA4]] (+0.80, fdr 7e-06); moves opposite to [[PSMG1]] (-0.64, fdr 1e-05), [[IPO5]] (-0.62, fdr 1e-05), [[SGPL1]] (-0.62, fdr 2e-05).
> It sits in the **+** arm of [[Module 048]] (Aerobic respiration and respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 6 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3395.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (A549 4.54×, SNU-1 6.68×, NCI-H1573 4.56×, PANC-1 3.92×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **2.55×** | +6.6 | 3e-08 | 46/49 (A549, SNU-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **2.20×** | +5.3 | 3e-05 | 32/43 (A549, AsPC-1, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.95×** | +4.5 | 0.001 | 43/47 (MIA PaCa-2, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **1.91×** | +4.2 | 0.004 | 34/45 (NCI-H460, J82, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | **1.64×** | +3.4 | 0.063 | 35/48 (NCI-H23, LoVo, …) | top dose only | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~56% of this change | **1.61×** | +3.3 | 0.077 | 33/48 (HOP62, NCI-H2347, …) | inconsistent across doses | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | 1.38× | +3.1 | 0.14 | 29/48 (AsPC-1, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~14% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3395.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (H4 0.381×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Diphenhydramine (drug)]] 0.05 µM |  | 0.633× | -3.0 | 0.47 | 43/48 (NCI-H460, AsPC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.27 per unit of S-phase module lfc, +0.47 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3395. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 48.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.54× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[H4 (line)]] | wt | 109 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.381× (z -8.7) |
| [[NCI-H1573 (line)]] | alt | 46.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.56× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[PANC-1 (line)]] | alt | 86.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.92× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[SNU-1 (line)]] | wt | 54.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.68× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[A-172 (line)]] | wt | 45.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 54.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 56.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 73.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 51.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 74.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 54.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 49.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 69.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 67.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 62.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 49.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 51.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 55.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 51.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 63.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 74.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 47.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 118 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 97.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 72.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 103 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 48.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 86.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 52.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 98.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 52.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 64.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 67.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 91.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 59.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 59.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 75.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 64.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 58.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 65.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 76.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 72.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 50.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 55.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3395), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 21 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDUFA1]] | +0.84 | +0.78 / +0.85 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 824 |
| [[COX6B1]] | +0.82 | +0.76 / +0.84 | both halves | 7e-06 | same gene group; pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 998 |
| [[NDUFB11]] ⚠ | +0.80 | +0.79 / +0.80 | both halves | 7e-06 | pathway: Aerobic respiration and respiratory electron transport; STRING 575; ⚠ in the vector space only through flagged drug-doses |
| [[NDUFA4]] | +0.80 | +0.67 / +0.85 | both halves | 7e-06 | same gene group; pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 997 |
| [[ROMO1]] | +0.77 | +0.67 / +0.83 | both halves | 7e-06 | STRING 570 |
| [[SERF2]] | +0.77 | +0.75 / +0.76 | both halves | 7e-06 | STRING 533 |
| [[MIF]] | +0.74 | +0.60 / +0.81 | both halves | 7e-06 |  |
| [[COX6C]] | +0.74 | +0.62 / +0.83 | both halves | 7e-06 | same gene group; pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 997 |
| [[UQCRQ]] ⚠ | +0.74 | +0.59 / +0.83 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 973; ⚠ in the vector space only through flagged drug-doses |
| [[ATP5MK]] | +0.74 | +0.63 / +0.80 | both halves | 7e-06 | pathway: Aerobic respiration and respiratory electron transport; STRING 724 |
| [[UBL5]] | +0.73 | +0.65 / +0.80 | both halves | 7e-06 | STRING 778 |
| [[COX7C]] | +0.73 | +0.57 / +0.81 | both halves | 9e-06 | same gene group; pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 997 |
| [[NDUFA2]] | +0.72 | +0.62 / +0.80 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 903 |
| [[SEC61G]] | +0.72 | +0.57 / +0.76 | both halves | 1e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMG1]] | -0.64 | -0.50 / -0.59 | both halves | 1e-05 |  |
| [[IPO5]] | -0.62 | -0.49 / -0.66 | both halves | 1e-05 |  |
| [[SGPL1]] | -0.62 | -0.47 / -0.65 | both halves | 2e-05 |  |
| [[FLII]] | -0.61 | -0.45 / -0.62 | both halves | 3e-05 |  |
| [[EIF3C]] | -0.61 | -0.48 / -0.59 | both halves | 2e-05 |  |
| [[PDAP1]] | -0.59 | -0.40 / -0.58 | both halves | 4e-05 |  |
| [[PUS7L]] | -0.58 | -0.37 / -0.58 | both halves | 8e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 048]] — Aerobic respiration and respiratory electron transport; 93 genes; this gene is in the **+** arm (projection on the module's main direction 0.831). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- ⚠ **In the space only through flagged drug-doses**: its significant pooled drug-doses and per-line responses all carry an alert (`embed/genes.parquet` evidence_flagged_only), so its module and partners may reflect what those drug-doses did to the cells.
- **Nodal map** (x, y) = (-46.5, -22.5); signed map (-35.1, 9.7). **Vector** length 65.6, 26.1% of its response variance represented; |z| ≥ 3 in 389 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Formation of ATP by chemiosmotic coupling* (reactome, mean cos +0.68 to 7); *Complex I biogenesis* (reactome, mean cos +0.64 to 9); *Cristae formation* (reactome, mean cos +0.68 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | +0.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.9 | +1.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +2.8 | +1.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | +2.5 | +3.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.2 | +1.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | +2.0 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.2 | +1.7 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.1 | +1.8 |
|  | [[Almonertinib (hydrochloride) (drug)]] 0.05 µM |  | +1.1 | +0.1 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | -4.3 | +5.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | -4.2 | +6.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | -4.2 | +4.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.8 | +0.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.7 | +1.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.7 | -0.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.3 | +1.4 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.6 | -2.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.5 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | cytochrome c oxidase subunit 7A2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q14.1 — chr6:75,237,675-75,250,323 (-) |
| Ensembl biotype | protein_coding |
| Also known as | COXVIIa-L, COX7AL |
| Gene groups (HGNC) | Mitochondrial complex IV: cytochrome c oxidase subunits |
| Hallmark sets | OXIDATIVE_PHOSPHORYLATION |
| Reactome | 9 pathways, smallest: Complex IV assembly; Cytoprotection by HMOX1; TP53 Regulates Metabolic Genes |
| Matched by | ensembl_id |

**Function**, from UniProt [P14406](https://www.uniprot.org/uniprotkb/P14406) (Cytochrome c oxidase subunit 7A2, mitochondrial):

> Component of the cytochrome c oxidase, the last enzyme in the mitochondrial electron transport chain which drives oxidative phosphorylation. The respiratory chain contains 3 multisubunit complexes succinate dehydrogenase (complex II, CII), ubiquinol-cytochrome c oxidoreductase (cytochrome b-c1 complex, complex III, CIII) and cytochrome c oxidase (complex IV, CIV), that cooperate to transfer electrons derived from NADH and succinate to molecular oxygen, creating an electrochemical gradient over …

**Summary**, from NCBI Gene [1347](https://www.ncbi.nlm.nih.gov/gene/1347):

> Cytochrome c oxidase, the terminal component of the mitochondrial respiratory chain, catalyzes the electron transfer from reduced cytochrome c to oxygen. This component is a heteromeric complex consisting of three catalytic subunits encoded by mitochondrial genes, and multiple structural subunits encoded by nuclear genes. The mitochondrially-encoded subunits function in electron transfer, while the nuclear-encoded subunits may function in the regulation and assembly of the complex. This nuclear …

**Accessions** — [HGNC:2288](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2288) · Entrez [1347](https://www.ncbi.nlm.nih.gov/gene/1347) · UniProt [P14406](https://www.uniprot.org/uniprotkb/P14406) · Ensembl [ENSG00000112695](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112695)

## Data

Gene col 3395: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3395); `tables/drug_effects.parquet` (8 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3395, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3395]; `tensor/DDL_lfc|DDL_z.npy` [3395]; `embed/gene_vectors.npy` [3395]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3395 or target_col == 3395). Every well: [[COX7A2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COX7A2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
