---
symbol: "PTCD1"
type: "gene"
col: 2733
ensembl_id: "ENSG00000106246"
name: "pentatricopeptide repeat domain 1"
location: "7q22.1"
module: 83
arm: "+"
pooled_cpm: 17.0
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 0
n_dd_up_clean: 6
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/083"]
generated_by: "tahoemap"
---

# PTCD1

*pentatricopeptide repeat domain 1* — 7q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.49× (z +11.2, q 2e-26, up in 32 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 2 lines (C32 0.256×, NCI-H460 0.393×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (Hs 766T 0.0934×); [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM in 1 line (SHP-77 0.0842×); [[Silodosin (drug)]] 5 µM in 1 line (HepG2/C3A 0.0956×).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPRYD4]] (+0.71, fdr 1e-05), [[UQCC1]] (+0.67, fdr 1e-05), [[GTF3C2-AS2]] (+0.65, fdr 2e-05); moves opposite to [[SPAG9]] (-0.60, fdr 3e-05), [[MAPK8]] (-0.52, fdr 2e-04).
> It sits in the **+** arm of [[Module 083]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 7 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2733.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +11.2 | 2e-26 | 32/47 (A498, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.74×** | +10.3 | 2e-22 | 29/43 (NCI-H1573, HT-29, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.43×** | +7.1 | 2e-10 | 23/48 (SW480, A-172, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.40×** | +6.6 | 5e-09 | 22/48 (PANC-1, LoVo, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.68×** | +5.4 | 1e-05 | 16/48 (LoVo, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.20×** | +5.2 | 2e-05 | 16/48 (BT-474, HOP62, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | 1.19× | +4.9 | 8e-05 | 17/48 (CFPAC-1, SW48, …) | top dose only | low cells (technical?) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +4.7 | 2e-04 | 19/47 (LoVo, NCI-H460, …) | rises with dose | composition shift |
| [[Triamcinolone (drug)]] 5 µM |  | 1.18× | +4.6 | 3e-04 | 8/48 (A498, NCI-H1573, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.22×** | +4.0 | 0.004 | 15/47 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Almonertinib (mesylate) (drug)]] 0.05 µM |  | **1.24×** | +3.9 | 0.006 | 9/47 (LoVo, RKO, …) | inconsistent across doses | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.21×** | +3.7 | 0.010 | 9/47 (A498, MIA PaCa-2, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | 1.19× | +3.5 | 0.021 | 9/48 (MIA PaCa-2, CFPAC-1, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.19× | +3.4 | 0.026 | 8/48 (PANC-1, AN3 CA, …) | two highest doses | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | 1.18× | +3.3 | 0.035 | 9/48 (MIA PaCa-2, A-172, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2733.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 2 lines (C32 0.256×, NCI-H460 0.393×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (Hs 766T 0.0934×); [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM in 1 line (SHP-77 0.0842×); [[Silodosin (drug)]] 5 µM in 1 line (HepG2/C3A 0.0956×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | 0.853× | -3.2 | 0.79 | 13/48 (NCI-H2030, BT-474, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2733. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 13.8 | 0 | 2 | — | [[Silodosin (drug)]] 5 µM 0.0956× (z -9.7) |
| [[NCI-H460 (line)]] | wt | 15.8 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +9.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Digitoxin (drug)]] 5 µM 0.393× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[A498 (line)]] | wt | 15.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.41× (z +10.2) | — |
| [[AsPC-1 (line)]] | alt | 8.87 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.131× (z -10.3) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[C32 (line)]] | wt | 39.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.256× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[Hs 766T (line)]] | wt | 15.6 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0934× (z -14.4) |
| [[LoVo (line)]] | wt | 20.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +9.8) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H1573 (line)]] | alt | 17.9 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 4.42× (z +10.0) ⚠ toxic | — |
| [[RKO (line)]] | wt | 25.0 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.252× (z -8.6) ⚠ cell-cycle shift, explains ~95% of this change |
| [[SHP-77 (line)]] | alt | 12.4 | 0 | 1 | — | [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM 0.0842× (z -13.4) |
| [[A-172 (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.00 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 31.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 24.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2733), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPRYD4]] | +0.71 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[UQCC1]] | +0.67 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[GTF3C2-AS2]] | +0.65 | +0.47 / +0.59 | both halves | 2e-05 |  |
| [[GPN2]] | +0.65 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[MAPKAPK5]] | +0.65 | +0.60 / +0.45 | both halves | 3e-05 |  |
| [[MAEA]] | +0.64 | +0.62 / +0.44 | both halves | 3e-05 |  |
| [[ACAD9]] | +0.64 | +0.61 / +0.48 | both halves | 2e-05 |  |
| [[EXOSC3]] | +0.63 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[AKAP8]] | +0.63 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[MAIP1]] | +0.62 | +0.60 / +0.40 | both halves | 5e-05 |  |
| [[CNPY2-AS1]] | +0.62 | +0.60 / +0.40 | both halves | 5e-05 |  |
| [[ZFHX2-AS1]] | +0.62 | +0.55 / +0.40 | both halves | 4e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPAG9]] | -0.60 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[MAPK8]] | -0.52 | -0.47 / -0.29 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 083]]; 53 genes; this gene is in the **+** arm (projection on the module's main direction 0.662). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (-8.4, 18.8); signed map (29.0, -19.3). **Vector** length 62.7, 8.73% of its response variance represented; |z| ≥ 3 in 871 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.5 | +10.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.6 | +7.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.9 | +11.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.0 | +2.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | +2.8 | +5.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +5.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.3 | +1.2 |
|  | [[EX229 (drug)]] 5 µM |  | +1.8 | +2.6 |
| fall | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.8 | -0.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~95% of this change | -2.7 | -2.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | +1.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.3 | -1.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -2.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.9 | -1.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.4 | +0.9 |
|  | [[Cyclosporin A (drug)]] 0.05 µM |  | -1.3 | -2.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.1 | -0.1 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.0 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | pentatricopeptide repeat domain 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q22.1 — chr7:99,416,739-99,466,163 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0632 |
| Gene groups (HGNC) | Pentatricopeptide repeat containing |
| Matched by | ensembl_id |

**Function**, from UniProt [O75127](https://www.uniprot.org/uniprotkb/O75127) (Pentatricopeptide repeat-containing protein 1, mitochondrial):

> Mitochondrial protein implicated in negative regulation of leucine tRNA levels, as well as negative regulation of mitochondria-encoded proteins and COX activity. Also affects the 3'-processing of mitochondrial tRNAs.

**Summary**, from NCBI Gene [26024](https://www.ncbi.nlm.nih.gov/gene/26024):

> This gene encodes a mitochondrial protein that binds leucine tRNAs and other mitochondrial RNAs and plays a role in the regulation of translation. Increased expression of this gene results in decreased mitochondrial leucine tRNA levels. Naturally occurring read-through transcription exists between upstream ATP5J2 (ATP synthase, H+ transporting, mitochondrial Fo complex, subunit F2) and this gene. [provided by RefSeq, Aug 2015]

**Accessions** — [HGNC:22198](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:22198) · Entrez [26024](https://www.ncbi.nlm.nih.gov/gene/26024) · UniProt [O75127](https://www.uniprot.org/uniprotkb/O75127) · Ensembl [ENSG00000106246](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106246)

## Data

Gene col 2733: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2733); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2733, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2733]; `tensor/DDL_lfc|DDL_z.npy` [2733]; `embed/gene_vectors.npy` [2733]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2733 or target_col == 2733). Every well: [[PTCD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PTCD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
