---
symbol: "RPS15"
type: "gene"
col: 3646
ensembl_id: "ENSG00000115268"
name: "ribosomal protein S15"
location: "19p13.3"
module: 131
arm: "+"
pooled_cpm: 134.0
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 0
n_dd_up_clean: 0
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/131", "evidence-flagged-only"]
generated_by: "tahoemap"
---

# RPS15

*ribosomal protein S15* — 19p13.3

## At a glance

> [!summary] In this data
> ⚠ It is in the vector space only through drug-doses that carry an alert for it (its significant pooled drug-doses and per-line responses; `embed/genes.parquet` evidence_flagged_only): its vector, partners and module rest on changes that may come from what those drug-doses did to the cells rather than from its own regulation.
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.02× (z +5.8, q 4e-06, up in 47 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change. None of them is without an alert.
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 23 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPS23]] (+0.94, fdr 7e-06), [[RPL8]] (+0.92, fdr 7e-06, ⚠ RPL8 in the vector space only through flagged drug-doses), [[RPS13]] (+0.91, fdr 7e-06, ⚠ RPS13 in the vector space only through flagged drug-doses), [[RPS10]] (+0.90, fdr 7e-06), [[RPS11]] (+0.90, fdr 7e-06); moves opposite to [[EIF4G1]] (-0.63, fdr 1e-05), [[NCBP1]] (-0.62, fdr 1e-05).
> It is in [[Module 131]], a single-armed module (Eukaryotic Translation Termination).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 7 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3646.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **3.02×** | +5.8 | 4e-06 | 47/49 (LoVo, A549, …) | all doses, flat | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~36% of this change | **2.12×** | +4.2 | 0.007 | 44/48 (SW1417, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.13×** | +3.9 | 0.017 | 46/47 (MIA PaCa-2, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **2.13×** | +3.8 | 0.017 | 35/44 (SW 900, NCI-H460, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **1.93×** | +3.7 | 0.025 | 42/48 (NCI-H460, SW480, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **2.18×** | +3.6 | 0.031 | 40/45 (MIA PaCa-2, HT-29, …) | all doses, flat | composition shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.21×** | +3.3 | 0.075 | 24/50 (C-33 A, BT-474, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3646.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | 0.666× | -3.3 | 0.54 | 29/48 (RKO, C-33 A, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, +0.50 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3646. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 136 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 170 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 124 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 106 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 148 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 126 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 96.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 153 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 84.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 80.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 130 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 64.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 73.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 161 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 149 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 116 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 85.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 108 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 136 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 105 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 84.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 99.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 206 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 149 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 141 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 184 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 85.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 93.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 204 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 245 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 171 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 130 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 141 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 251 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 205 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 91.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 90.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 142 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 98.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 152 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 224 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 140 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3646), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 23 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPS23]] | +0.94 | +0.92 / +0.93 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999 |
| [[RPL8]] ⚠ | +0.92 | +0.90 / +0.92 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPS13]] ⚠ | +0.91 | +0.85 / +0.91 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPS10]] | +0.90 | +0.87 / +0.91 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999 |
| [[RPS11]] | +0.90 | +0.85 / +0.89 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999 |
| [[RPL15]] | +0.89 | +0.78 / +0.93 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL38]] | +0.89 | +0.89 / +0.88 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS29]] | +0.88 | +0.81 / +0.90 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999 |
| [[RPL28]] | +0.88 | +0.81 / +0.90 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[FAU]] | +0.88 | +0.74 / +0.92 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999 |
| [[RPL32]] | +0.87 | +0.82 / +0.87 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS21]] | +0.87 | +0.78 / +0.89 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999 |
| [[RPL36A]] | +0.86 | +0.78 / +0.87 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 996 |
| [[RPL7A]] | +0.86 | +0.74 / +0.89 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF4G1]] | -0.63 | -0.52 / -0.63 | both halves | 1e-05 | pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 895 |
| [[NCBP1]] | -0.62 | -0.51 / -0.69 | both halves | 1e-05 | pathway: Nonsense Mediated Decay (NMD) enhanced by the Exon Junction Complex (EJC) |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 131]] — Eukaryotic Translation Termination; 36 genes; every member is in the + arm (projection on the module's main direction 0.925). A single-armed module: all its genes lie on one side of its main direction.
- ⚠ **In the space only through flagged drug-doses**: its significant pooled drug-doses and per-line responses all carry an alert (`embed/genes.parquet` evidence_flagged_only), so its module and partners may reflect what those drug-doses did to the cells.
- **Nodal map** (x, y) = (-47.4, -27.0); signed map (-62.0, -2.9). **Vector** length 81.2, 47.8% of its response variance represented; |z| ≥ 3 in 340 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Ribosome Quality Control (RQC) complex extracts and degrades nascent peptide* (reactome, mean cos +0.88 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.4 | +0.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.0 | +1.2 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +2.5 | +3.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.3 | +0.2 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +2.2 | +1.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.1 | +2.3 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.9 | +1.5 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | -6.2 | +3.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | -6.2 | +5.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | -5.9 | +3.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.8 | +0.4 |
|  | [[Trifluridine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | -0.8 |
|  | [[Hesperidin (drug)]] 0.05 µM |  | -1.7 | -0.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.6 | -2.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.6 | +0.5 |
|  | [[Gallic acid (hydrate) (drug)]] 0.5 µM |  | -1.6 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal protein S15 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:1,438,358-1,440,495 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RIG, MGC111130, S15, uS19 |
| Gene groups (HGNC) | S ribosomal proteins |
| Reactome | 51 pathways, smallest: SARS-CoV-1 modulates host translation machinery; SARS-CoV-2 modulates host translation machinery; Formation of the ternary complex, and subsequently, the 43S complex |
| Matched by | ensembl_id |

**Function**, from UniProt [P62841](https://www.uniprot.org/uniprotkb/P62841) (Small ribosomal subunit protein uS19):

> Component of the small ribosomal subunit. The ribosome is a large ribonucleoprotein complex responsible for the synthesis of proteins in the cell.

**Summary**, from NCBI Gene [6209](https://www.ncbi.nlm.nih.gov/gene/6209):

> Ribosomes, the organelles that catalyze protein synthesis, consist of a small 40S subunit and a large 60S subunit. Together these subunits are composed of 4 RNA species and approximately 80 structurally distinct proteins. This gene encodes a ribosomal protein that is a component of the 40S subunit. The protein belongs to the S19P family of ribosomal proteins. It is located in the cytoplasm. This gene has been found to be activated in various tumors, such as insulinomas, esophageal cancers, and …

**Accessions** — [HGNC:10388](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10388) · Entrez [6209](https://www.ncbi.nlm.nih.gov/gene/6209) · UniProt [P62841](https://www.uniprot.org/uniprotkb/P62841) · Ensembl [ENSG00000115268](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115268)

## Data

Gene col 3646: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3646); `tables/drug_effects.parquet` (8 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3646, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3646]; `tensor/DDL_lfc|DDL_z.npy` [3646]; `embed/gene_vectors.npy` [3646]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3646 or target_col == 3646). Every well: [[RPS15 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPS15.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
