---
symbol: "TMEM258"
type: "gene"
col: 5610
ensembl_id: "ENSG00000134825"
name: "transmembrane protein 258"
location: "11q12.2"
module: 24
arm: "+"
pooled_cpm: 43.12
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 2
n_dd_up_clean: 0
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# TMEM258

*transmembrane protein 258* — 11q12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.00× (z +4.2, q 0.017, up in 39 of 46 measured lines) ⚠ toxic; transcription drop.
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.540× (z -5.2, q 1e-04, down in 39 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (RKO 0.256×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 21 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPL36AL]] (+0.84, fdr 7e-06, ⚠ RPL36AL in the vector space only through flagged drug-doses), [[LAMTOR5]] (+0.81, fdr 7e-06), [[COX6B1]] (+0.81, fdr 7e-06), [[NDUFA1]] (+0.79, fdr 7e-06); moves opposite to [[YWHAQ]] (-0.73, fdr 7e-06), [[CAPRIN1]] (-0.72, fdr 7e-06), [[LIN7C]] (-0.71, fdr 1e-05).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 2 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5610.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.00×** | +4.2 | 0.017 | 39/46 (C-33 A, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~21% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~44% of this change | 1.76× | +3.4 | 0.20 | 35/47 (CFPAC-1, NCI-H2030, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5610.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (RKO 0.256×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.540×** | -5.2 | 1e-04 | 39/47 (RKO, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.538×** | -3.7 | 0.059 | 39/48 (NCI-H1573, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 5 µM |  | 0.587× | -3.2 | 0.23 | 37/48 (NCI-H1792, H4, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Diphenhydramine (drug)]] 0.05 µM |  | 0.565× | -3.1 | 0.23 | 44/48 (LoVo, RKO, …) | inconsistent across doses |  |
| [[Erlotinib (drug)]] 0.05 µM |  | 0.570× | -3.1 | 0.23 | 40/48 (LoVo, J82, …) | inconsistent across doses | position effect removed |
| [[Lucanthone (drug)]] 0.05 µM |  | 0.576× | -3.0 | 0.23 | 36/48 (NCI-H1792, SNU-423, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, +0.59 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5610. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 39.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.256× (z -8.9) |
| [[A-172 (line)]] | wt | 39.3 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 53.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 35.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 35.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 29.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 33.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 48.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 51.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 31.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 50.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 52.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 64.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 36.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 44.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 90.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 38.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 25.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 47.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 49.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 60.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 50.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 27.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 41.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 47.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 49.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 49.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 31.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 48.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 46.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 44.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 54.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 32.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 51.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5610), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 21 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPL36AL]] ⚠ | +0.84 | +0.78 / +0.86 | both halves | 7e-06 | pathway: Cotranslational targeting of proteins to the endoplasmic reticulum; ⚠ in the vector space only through flagged drug-doses |
| [[LAMTOR5]] | +0.81 | +0.74 / +0.87 | both halves | 7e-06 |  |
| [[COX6B1]] | +0.81 | +0.66 / +0.86 | both halves | 7e-06 |  |
| [[SMIM26]] ⚠ | +0.79 | +0.63 / +0.83 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[NDUFA1]] | +0.79 | +0.73 / +0.83 | both halves | 7e-06 |  |
| [[RPL36]] | +0.79 | +0.70 / +0.83 | both halves | 7e-06 | pathway: Cotranslational targeting of proteins to the endoplasmic reticulum |
| [[KRT10]] ⚠ | +0.78 | +0.73 / +0.79 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[COMMD6]] | +0.78 | +0.69 / +0.83 | both halves | 7e-06 |  |
| [[SEC61G]] | +0.78 | +0.68 / +0.82 | both halves | 7e-06 | pathway: Cotranslational targeting of proteins to the endoplasmic reticulum; STRING 896 |
| [[SNHG9]] | +0.77 | +0.58 / +0.79 | both halves | 8e-06 |  |
| [[RPS27]] | +0.75 | +0.61 / +0.81 | both halves | 7e-06 | pathway: Cotranslational targeting of proteins to the endoplasmic reticulum |
| [[RPS19]] | +0.75 | +0.64 / +0.80 | both halves | 7e-06 | same gene group; pathway: Cotranslational targeting of proteins to the endoplasmic reticulum |
| [[ATP5MK]] | +0.75 | +0.67 / +0.81 | both halves | 7e-06 | same gene group |
| [[INAFM1]] | +0.75 | +0.60 / +0.81 | both halves | 7e-06 |  |
| [[TOMM7]] | +0.75 | +0.66 / +0.81 | both halves | 7e-06 | pathway: Protein localization; STRING 434 |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YWHAQ]] | -0.73 | -0.58 / -0.81 | both halves | 7e-06 | pathway: SARS-CoV-2 Infection |
| [[CAPRIN1]] | -0.72 | -0.59 / -0.75 | both halves | 7e-06 |  |
| [[LIN7C]] | -0.71 | -0.52 / -0.78 | both halves | 1e-05 |  |
| [[MOB1A]] | -0.70 | -0.57 / -0.76 | both halves | 1e-05 |  |
| [[IPO5]] | -0.70 | -0.54 / -0.72 | both halves | 1e-05 |  |
| [[CCT7]] | -0.69 | -0.66 / -0.69 | both halves | 7e-06 |  |
| [[NRAS]] | -0.69 | -0.48 / -0.69 | both halves | 2e-05 |  |
| [[CCT5]] | -0.69 | -0.68 / -0.65 | both halves | 7e-06 |  |
| [[MAPRE1]] | -0.68 | -0.50 / -0.74 | both halves | 1e-05 |  |
| [[PSME3]] | -0.68 | -0.60 / -0.69 | both halves | 7e-06 |  |
| [[DARS2]] | -0.68 | -0.60 / -0.70 | both halves | 7e-06 |  |
| [[VMA21]] | -0.68 | -0.49 / -0.74 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.806). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-43.1, -21.3); signed map (-32.0, 9.0). **Vector** length 80.7, 32.0% of its response variance represented; |z| ≥ 3 in 404 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Aerobic respiration and respiratory electron transport* (reactome, mean cos +0.50 to 12).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.7 | +2.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.5 | +1.1 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.2 | +2.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.1 | +0.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.0 | +1.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +2.9 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | +1.9 | +2.3 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | +1.8 | +2.6 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.1 | +2.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.8 | +2.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.7 | +4.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.6 | +0.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.5 | -0.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -2.2 | -1.6 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -1.7 | -0.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.7 | -1.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.6 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 258 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q12.2 — chr11:61,768,501-61,792,802 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Kuduk, Kud; previously C11orf10 |
| Gene groups (HGNC) | Oligosaccharyltransferase complex subunits; MicroRNA protein coding host genes |
| Reactome | 26 pathways, smallest: PD-L1(CD274) glycosylation and translocation to plasma membrane; Regulation of CDH1 posttranslational processing and trafficking to plasma membrane; Maturation of spike protein_9694548 |
| Matched by | ensembl_id |

**Function**, from UniProt [P61165](https://www.uniprot.org/uniprotkb/P61165) (Dolichyl-diphosphooligosaccharide--protein glycosyltransferase subunit TMEM258):

> Subunit of the oligosaccharyl transferase (OST) complex that catalyzes the initial transfer of a defined glycan (Glc(3)Man(9)GlcNAc(2) in eukaryotes) from the lipid carrier dolichol-pyrophosphate to an asparagine residue within an Asn-Xaa-Ser/Thr consensus motif in nascent polypeptide chains, the first step in protein N-glycosylation. N-glycosylation occurs cotranslationally and the complex associates with the Sec61 complex at the channel-forming translocon complex that mediates protein …

**Summary**, from NCBI Gene [746](https://www.ncbi.nlm.nih.gov/gene/746):

> Predicted to enable oligosaccharyltransferase complex binding activity. Involved in protein N-linked glycosylation. Acts upstream of or within protein secretion and response to endoplasmic reticulum stress. Located in endoplasmic reticulum and membrane. Part of oligosaccharyltransferase complex A and oligosaccharyltransferase complex B. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:1164](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1164) · Entrez [746](https://www.ncbi.nlm.nih.gov/gene/746) · UniProt [P61165](https://www.uniprot.org/uniprotkb/P61165) · Ensembl [ENSG00000134825](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134825)

## Data

Gene col 5610: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5610); `tables/drug_effects.parquet` (8 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5610, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5610]; `tensor/DDL_lfc|DDL_z.npy` [5610]; `embed/gene_vectors.npy` [5610]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5610 or target_col == 5610). Every well: [[TMEM258 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM258.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
