---
symbol: "RPS13"
type: "gene"
col: 3157
ensembl_id: "ENSG00000110700"
name: "ribosomal protein S13"
location: "11p15.1"
module: 131
arm: "+"
pooled_cpm: 290.84
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 0
n_dd_up_clean: 0
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/131", "evidence-flagged-only"]
generated_by: "tahoemap"
---

# RPS13

*ribosomal protein S13* — 11p15.1

## At a glance

> [!summary] In this data
> ⚠ It is in the vector space only through drug-doses that carry an alert for it (its significant pooled drug-doses and per-line responses; `embed/genes.parquet` evidence_flagged_only): its vector, partners and module rest on changes that may come from what those drug-doses did to the cells rather than from its own regulation.
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.78× (z +5.1, q 2e-04, up in 48 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change. None of them is without an alert.
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 23 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPS29]] (+0.94, fdr 7e-06), [[RPS8]] (+0.94, fdr 7e-06), [[RPL15]] (+0.94, fdr 7e-06); moves opposite to [[PNPO]] (-0.72, fdr 7e-06).
> It is in [[Module 131]], a single-armed module (Eukaryotic Translation Termination).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 6 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3157.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **2.78×** | +5.1 | 2e-04 | 48/49 (COLO 205, A549, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **2.08×** | +4.2 | 0.008 | 42/44 (A-172, Hs 766T, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.02×** | +4.0 | 0.012 | 45/47 (RKO, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~39% of this change | **1.89×** | +3.8 | 0.023 | 43/48 (SW 900, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **1.80×** | +3.5 | 0.056 | 45/48 (NCI-H460, NCI-H1792, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | 1.87× | +3.1 | 0.21 | 36/45 (CFPAC-1, HT-29, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3157.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Folic acid (drug)]] 5 µM |  | 0.685× | -3.1 | 0.61 | 45/48 (COLO 205, CFPAC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | 0.692× | -3.1 | 0.61 | 33/48 (C-33 A, CHP-212, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, +0.46 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3157. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 162 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 313 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 281 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 343 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 284 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 333 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 162 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 265 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 148 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 171 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 144 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 139 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 320 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 284 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 237 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 279 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 259 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 392 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 243 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 416 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 258 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 256 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 179 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 593 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 438 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 310 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 284 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 150 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 233 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 231 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 227 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 196 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 420 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 259 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 316 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 229 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 482 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 308 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 322 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 206 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 255 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 346 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 324 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 181 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 263 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 375 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 417 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 374 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3157), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 23 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPS29]] | +0.94 | +0.90 / +0.95 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999 |
| [[RPS8]] | +0.94 | +0.89 / +0.96 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999 |
| [[RPL15]] | +0.94 | +0.88 / +0.96 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL32]] | +0.94 | +0.91 / +0.94 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS27A]] ⚠ | +0.94 | +0.91 / +0.95 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPL36A]] | +0.94 | +0.90 / +0.93 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 996 |
| [[RPS10]] | +0.93 | +0.91 / +0.95 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999 |
| [[RPL28]] | +0.93 | +0.89 / +0.94 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL31]] | +0.93 | +0.85 / +0.96 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS16]] ⚠ | +0.93 | +0.91 / +0.94 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPL8]] ⚠ | +0.93 | +0.90 / +0.93 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPS25]] | +0.93 | +0.86 / +0.95 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999 |
| [[RPL35A]] | +0.92 | +0.87 / +0.94 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL34]] | +0.92 | +0.86 / +0.93 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPLP2]] | +0.92 | +0.87 / +0.94 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PNPO]] | -0.72 | -0.63 / -0.70 | both halves | 7e-06 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 131]] — Eukaryotic Translation Termination; 36 genes; every member is in the + arm (projection on the module's main direction 0.959). A single-armed module: all its genes lie on one side of its main direction.
- ⚠ **In the space only through flagged drug-doses**: its significant pooled drug-doses and per-line responses all carry an alert (`embed/genes.parquet` evidence_flagged_only), so its module and partners may reflect what those drug-doses did to the cells.
- **Nodal map** (x, y) = (-46.6, -27.2); signed map (-61.3, -3.4). **Vector** length 86.4, 58.6% of its response variance represented; |z| ≥ 3 in 365 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Ribosome Quality Control (RQC) complex extracts and degrades nascent peptide* (reactome, mean cos +0.93 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.8 | +0.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +0.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.5 | +1.9 |
|  | [[Temsirolimus (drug)]] 5 µM |  | +2.3 | +0.8 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.3 | +0.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.2 | -0.8 |
|  | [[Rapamycin (drug)]] 0.05 µM |  | +2.0 | +0.8 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | -7.1 | +5.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | -6.9 | +3.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | -6.8 | +4.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.9 | -0.5 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~39% of this change | -2.8 | +3.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.5 | +1.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.0 | -0.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.9 | -2.1 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.8 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal protein S13 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.1 — chr11:17,074,388-17,077,715 (-) |
| Ensembl biotype | protein_coding |
| Also known as | S13, uS15 |
| Gene groups (HGNC) | S ribosomal proteins; Small nucleolar RNA protein coding host genes |
| Reactome | 51 pathways, smallest: SARS-CoV-1 modulates host translation machinery; SARS-CoV-2 modulates host translation machinery; Formation of the ternary complex, and subsequently, the 43S complex |
| Matched by | ensembl_id |

**Function**, from UniProt [P62277](https://www.uniprot.org/uniprotkb/P62277) (Small ribosomal subunit protein uS15):

> Component of the small ribosomal subunit. The ribosome is a large ribonucleoprotein complex responsible for the synthesis of proteins in the cell. Part of the small subunit (SSU) processome, first precursor of the small eukaryotic ribosomal subunit. During the assembly of the SSU processome in the nucleolus, many ribosome biogenesis factors, an RNA chaperone and ribosomal proteins associate with the nascent pre-rRNA and work in concert to generate RNA folding, modifications, rearrangements and …

**Summary**, from NCBI Gene [6207](https://www.ncbi.nlm.nih.gov/gene/6207):

> Ribosomes, the organelles that catalyze protein synthesis, consist of a small 40S subunit and a large 60S subunit. Together these subunits are composed of 4 RNA species and approximately 80 structurally distinct proteins. This gene encodes a ribosomal protein that is a component of the 40S subunit. The protein belongs to the S15P family of ribosomal proteins. It is located in the cytoplasm. The protein has been shown to bind to the 5.8S rRNA in rat. The gene product of the E. coli ortholog …

**Accessions** — [HGNC:10386](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10386) · Entrez [6207](https://www.ncbi.nlm.nih.gov/gene/6207) · UniProt [P62277](https://www.uniprot.org/uniprotkb/P62277) · Ensembl [ENSG00000110700](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000110700)

## Data

Gene col 3157: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3157); `tables/drug_effects.parquet` (8 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3157, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3157]; `tensor/DDL_lfc|DDL_z.npy` [3157]; `embed/gene_vectors.npy` [3157]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3157 or target_col == 3157). Every well: [[RPS13 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPS13.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
