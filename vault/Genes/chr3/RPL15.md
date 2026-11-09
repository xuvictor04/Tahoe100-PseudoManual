---
symbol: "RPL15"
type: "gene"
col: 10521
ensembl_id: "ENSG00000174748"
name: "ribosomal protein L15"
location: "3p24.2"
module: 131
arm: "+"
pooled_cpm: 310.32
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 0
n_dd_up_clean: 0
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/131"]
generated_by: "tahoemap"
---

# RPL15

*ribosomal protein L15* — 3p24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.51× (z +5.7, q 6e-06, up in 45 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (COLO 205 5.48×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (C-33 A 0.349×, RKO 0.365×, A-427 0.417×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 23 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPS13]] (+0.94, fdr 7e-06, ⚠ RPS13 in the vector space only through flagged drug-doses), [[RPL7A]] (+0.92, fdr 7e-06), [[RPS8]] (+0.92, fdr 7e-06), [[RPL36A]] (+0.91, fdr 7e-06); moves opposite to [[SAE1]] (-0.63, fdr 1e-05), [[NCBP1]] (-0.63, fdr 1e-05).
> It is in [[Module 131]], a single-armed module (Eukaryotic Translation Termination).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 5 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10521.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (COLO 205 5.48×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **2.51×** | +5.7 | 6e-06 | 45/49 (COLO 205, A-172, …) | all doses, flat | composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **2.12×** | +4.8 | 4e-04 | 37/44 (NCI-H460, Hs 766T, …) | all doses, flat | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~34% of this change | **1.83×** | +4.6 | 9e-04 | 45/48 (KATO III, A-172, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.92×** | +4.2 | 0.003 | 45/47 (CFPAC-1, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **1.78×** | +4.0 | 0.007 | 34/45 (A-172, SNU-423, …) | all doses, flat | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10521.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (C-33 A 0.349×, RKO 0.365×, A-427 0.417×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | 0.719× | -3.5 | 0.24 | 30/48 (C-33 A, RKO, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.660× | -3.1 | 0.49 | 45/48 (LS 180, hTERT-HPNE, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, +0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10521. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 333 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.417× (z -8.8) |
| [[C-33 A (line)]] | alt | 287 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -10.7) |
| [[COLO 205 (line)]] | alt | 134 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.48× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[RKO (line)]] | wt | 404 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.365× (z -9.3) |
| [[A-172 (line)]] | wt | 210 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 194 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 352 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 324 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 224 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 249 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 177 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 192 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 290 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 209 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 346 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 467 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 313 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 449 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 193 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 315 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 255 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 335 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 265 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 312 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 460 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 440 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 406 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 261 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 154 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 310 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 303 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 246 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 272 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 592 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 268 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 327 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 249 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 393 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 226 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 290 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 205 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 322 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 293 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 394 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 252 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 382 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 191 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 427 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 482 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 313 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10521), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 23 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPS13]] ⚠ | +0.94 | +0.88 / +0.96 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPL7A]] | +0.92 | +0.89 / +0.95 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS8]] | +0.92 | +0.86 / +0.93 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL36A]] | +0.91 | +0.87 / +0.92 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 997 |
| [[RPL24]] | +0.91 | +0.81 / +0.92 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS23]] | +0.91 | +0.79 / +0.94 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL32]] | +0.91 | +0.84 / +0.93 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL8]] ⚠ | +0.90 | +0.87 / +0.93 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPL28]] | +0.90 | +0.84 / +0.93 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL19]] | +0.89 | +0.81 / +0.90 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS10]] | +0.89 | +0.82 / +0.94 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS15]] ⚠ | +0.89 | +0.78 / +0.93 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPS29]] | +0.89 | +0.76 / +0.92 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS25]] | +0.89 | +0.83 / +0.93 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS11]] | +0.88 | +0.78 / +0.89 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SAE1]] | -0.63 | -0.49 / -0.64 | both halves | 1e-05 |  |
| [[NCBP1]] | -0.63 | -0.51 / -0.66 | both halves | 1e-05 | pathway: Nonsense Mediated Decay (NMD) enhanced by the Exon Junction Complex (EJC) |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 131]] — Eukaryotic Translation Termination; 36 genes; every member is in the + arm (projection on the module's main direction 0.914). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-47.0, -27.4); signed map (-61.8, -3.5). **Vector** length 82.7, 52.8% of its response variance represented; |z| ≥ 3 in 387 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *SARS-CoV-2 modulates host translation machinery* (reactome, mean cos +0.86 to 12); *SARS-CoV-1 modulates host translation machinery* (reactome, mean cos +0.88 to 11); *Formation of the ternary complex, and subsequently, the 43S complex* (reactome, mean cos +0.88 to 11).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.1 | +2.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.0 | +1.3 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.5 | +0.5 |
|  | [[Temsirolimus (drug)]] 5 µM |  | +2.3 | +1.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.2 | +1.8 |
|  | [[AZD-8055 (drug)]] 0.5 µM |  | +2.1 | +0.1 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | -7.4 | +5.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | -7.2 | +4.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | -7.1 | +4.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.0 | +1.5 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~34% of this change | -2.9 | +4.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.1 | -0.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.1 | -0.2 |
|  | [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | -1.5 | -0.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.4 | +0.5 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal protein L15 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p24.2 — chr3:23,916,591-23,924,374 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RPL10, RPLY10, RPYL10, EC45, L15, eL15 |
| Gene groups (HGNC) | L ribosomal proteins |
| Reactome | 37 pathways, smallest: Peptide chain elongation; PELO:HBS1L and ABCE1 dissociate a ribosome on a non-stop mRNA; Viral mRNA Translation |
| Matched by | ensembl_id |

**Function**, from UniProt [P61313](https://www.uniprot.org/uniprotkb/P61313) (Large ribosomal subunit protein eL15):

> Component of the large ribosomal subunit. The ribosome is a large ribonucleoprotein complex responsible for the synthesis of proteins in the cell.

**Summary**, from NCBI Gene [6138](https://www.ncbi.nlm.nih.gov/gene/6138):

> Ribosomes, the organelles that catalyze protein synthesis, consist of a small 40S subunit and a large 60S subunit. Together these subunits are composed of four RNA species and approximately 80 structurally distinct proteins. This gene encodes a member of the L15E family of ribosomal proteins and a component of the 60S subunit. This gene shares sequence similarity with the yeast ribosomal protein YL10 gene. Elevated expression of this gene has been observed in esophageal tumors and gastric …

**Accessions** — [HGNC:10306](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10306) · Entrez [6138](https://www.ncbi.nlm.nih.gov/gene/6138) · UniProt [P61313](https://www.uniprot.org/uniprotkb/P61313) · Ensembl [ENSG00000174748](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000174748)

## Data

Gene col 10521: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10521); `tables/drug_effects.parquet` (7 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10521, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10521]; `tensor/DDL_lfc|DDL_z.npy` [10521]; `embed/gene_vectors.npy` [10521]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10521 or target_col == 10521). Every well: [[RPL15 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPL15.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
