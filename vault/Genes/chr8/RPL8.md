---
symbol: "RPL8"
type: "gene"
col: 8410
ensembl_id: "ENSG00000161016"
name: "ribosomal protein L8"
location: "8q24.3"
module: 131
arm: "+"
pooled_cpm: 267.42
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

# RPL8

*ribosomal protein L8* — 8q24.3

## At a glance

> [!summary] In this data
> ⚠ It is in the vector space only through drug-doses that carry an alert for it (its significant pooled drug-doses and per-line responses; `embed/genes.parquet` evidence_flagged_only): its vector, partners and module rest on changes that may come from what those drug-doses did to the cells rather than from its own regulation.
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.86× (z +6.4, q 7e-08, up in 42 of 44 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change. None of them is without an alert.
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 21 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPL32]] (+0.94, fdr 7e-06), [[RPS23]] (+0.93, fdr 7e-06), [[RPS13]] (+0.93, fdr 7e-06, ⚠ RPS13 in the vector space only through flagged drug-doses), [[RPL7A]] (+0.92, fdr 7e-06); moves opposite to [[PNPO]] (-0.63, fdr 3e-05).
> It is in [[Module 131]], a single-armed module (Eukaryotic Translation Termination).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 7 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8410.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **2.86×** | +6.4 | 7e-08 | 42/44 (H4, A498, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **3.81×** | +5.8 | 2e-06 | 49/49 (NCI-H460, SW480, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **2.46×** | +5.3 | 2e-05 | 43/45 (A-172, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~42% of this change | **1.98×** | +4.3 | 0.002 | 45/48 (SW 900, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.20×** | +3.8 | 0.014 | 24/50 (AsPC-1, KATO III, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.83×** | +3.7 | 0.021 | 42/47 (HepG2/C3A, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | **1.69×** | +3.3 | 0.074 | 37/48 (NCI-H460, NCI-H1573, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8410.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | 0.703× | -3.2 | 0.73 | 28/48 (A-427, RKO, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, +0.54 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8410. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 114 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 286 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 287 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 310 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 229 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 331 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 232 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 201 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 142 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 193 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 179 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 172 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 285 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 230 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 199 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 270 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 293 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 335 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 273 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 211 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 200 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 265 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 376 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 409 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 306 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 315 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 217 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 322 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 203 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 310 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 513 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 190 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 260 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 157 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 348 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 241 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 627 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 169 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 274 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 165 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 262 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 201 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 155 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 141 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 216 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 290 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 332 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 224 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8410), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 21 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPL32]] | +0.94 | +0.89 / +0.93 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS23]] | +0.93 | +0.90 / +0.94 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS13]] ⚠ | +0.93 | +0.90 / +0.93 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPL7A]] | +0.92 | +0.87 / +0.92 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS16]] ⚠ | +0.92 | +0.85 / +0.93 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPL28]] | +0.92 | +0.88 / +0.92 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS10]] | +0.92 | +0.90 / +0.90 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS15]] ⚠ | +0.92 | +0.90 / +0.92 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPS11]] | +0.91 | +0.87 / +0.92 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL15]] | +0.90 | +0.87 / +0.93 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS25]] | +0.90 | +0.80 / +0.91 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS21]] | +0.89 | +0.80 / +0.90 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS8]] | +0.89 | +0.83 / +0.91 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL38]] | +0.89 | +0.87 / +0.88 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS5]] | +0.88 | +0.79 / +0.91 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PNPO]] | -0.63 | -0.46 / -0.65 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 131]] — Eukaryotic Translation Termination; 36 genes; every member is in the + arm (projection on the module's main direction 0.922). A single-armed module: all its genes lie on one side of its main direction.
- ⚠ **In the space only through flagged drug-doses**: its significant pooled drug-doses and per-line responses all carry an alert (`embed/genes.parquet` evidence_flagged_only), so its module and partners may reflect what those drug-doses did to the cells.
- **Nodal map** (x, y) = (-47.2, -27.3); signed map (-61.9, -3.3). **Vector** length 75.2, 49.4% of its response variance represented; |z| ≥ 3 in 377 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *SARS-CoV-2 modulates host translation machinery* (reactome, mean cos +0.88 to 12); *SARS-CoV-1 modulates host translation machinery* (reactome, mean cos +0.89 to 11); *Formation of the ternary complex, and subsequently, the 43S complex* (reactome, mean cos +0.89 to 11).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.9 | +0.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.7 | +0.9 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +2.2 | +3.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.0 | +2.5 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.0 | +1.3 |
|  | [[Rapamycin (drug)]] 5 µM |  | +1.9 | +0.5 |
|  | [[Temsirolimus (drug)]] 5 µM |  | +1.9 | +0.6 |
|  | [[Rapamycin (drug)]] 0.05 µM |  | +1.6 | +0.5 |
|  | [[AZD-8055 (drug)]] 0.5 µM |  | +1.5 | -0.3 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | -7.0 | +5.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | -6.6 | +6.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | -6.0 | +5.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.0 | +1.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.0 | -0.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.0 | -0.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.6 | +0.4 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -1.5 | +0.2 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal protein L8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.3 — chr8:144,789,765-144,792,587 (-) |
| Ensembl biotype | protein_coding |
| Also known as | L8, uL2 |
| Gene groups (HGNC) | L ribosomal proteins; MicroRNA protein coding host genes |
| Reactome | 39 pathways, smallest: Protein hydroxylation; Gamma carboxylation, hypusinylation, hydroxylation, and arylsulfatase activation; Peptide chain elongation |
| Matched by | ensembl_id |

**Function**, from UniProt [P62917](https://www.uniprot.org/uniprotkb/P62917) (Large ribosomal subunit protein uL2):

> Component of the large ribosomal subunit. The ribosome is a large ribonucleoprotein complex responsible for the synthesis of proteins in the cell.

**Summary**, from NCBI Gene [6132](https://www.ncbi.nlm.nih.gov/gene/6132):

> Ribosomes, the organelles that catalyze protein synthesis, consist of a small 40S subunit and a large 60S subunit. Together these subunits are composed of 4 RNA species and approximately 80 structurally distinct proteins. This gene encodes a ribosomal protein that is a component of the 60S subunit. The protein belongs to the L2P family of ribosomal proteins. It is located in the cytoplasm. In rat, the protein associates with the 5.8S rRNA, very likely participates in the binding of …

**Accessions** — [HGNC:10368](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10368) · Entrez [6132](https://www.ncbi.nlm.nih.gov/gene/6132) · UniProt [P62917](https://www.uniprot.org/uniprotkb/P62917) · Ensembl [ENSG00000161016](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000161016)

## Data

Gene col 8410: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8410); `tables/drug_effects.parquet` (8 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8410, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8410]; `tensor/DDL_lfc|DDL_z.npy` [8410]; `embed/gene_vectors.npy` [8410]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8410 or target_col == 8410). Every well: [[RPL8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPL8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
