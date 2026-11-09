---
symbol: "CNGB3"
type: "gene"
col: 9928
ensembl_id: "ENSG00000170289"
name: "cyclic nucleotide gated channel subunit beta 3"
location: "8q21.3"
module: 21
arm: "+"
pooled_cpm: 5.63
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 1
n_dd_up_clean: 8
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# CNGB3

*cyclic nucleotide gated channel subunit beta 3* — 8q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.73× (z +11.8, q 3e-29, up in 29 of 29 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.84× (z +10.1, q 2e-21, up in 32 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.826× (z -7.8, q 4e-12, down in 29 of 48 measured lines) ⚠ position not correctable.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Pyridoxine (drug)]] 0.5 µM in 1 line (CFPAC-1 0.0891×); [[Arbutin (drug)]] 0.05 µM in 1 line (KATO III 0.0856×); [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM in 1 line (A549 0.0988×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HSPA2-AS1]] (+0.82, fdr 7e-06), [[CHMP3-AS1]] (+0.82, fdr 7e-06), [[LRRC37A16P]] (+0.82, fdr 7e-06).
> It is in [[Module 021]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 7 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9928.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.73×** | +11.8 | 3e-29 | 29/29 (A-172, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.78×** | +11.5 | 2e-28 | 7/8 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.84×** | +10.1 | 2e-21 | 32/41 (A498, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.23×** | +8.7 | 6e-16 | 11/16 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.69×** | +6.2 | 8e-08 | 20/36 (C32, HOP62, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~10% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.51×** | +4.6 | 4e-04 | 16/39 (MIA PaCa-2, RKO, …) | top dose only | cell-cycle shift (explains ~2% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +4.3 | 0.002 | 8/39 (SNU-423, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.26×** | +3.9 | 0.008 | 11/41 (A498, C32, …) | top dose only | composition shift; position effect removed |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.53×** | +3.6 | 0.022 | 2/44 (COLO 205, SK-MEL-2) | inconsistent across doses | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[Bendamustine (drug)]] 5 µM |  | **1.34×** | +3.3 | 0.060 | 8/42 (HEC-1-A, HOP62, …) | top dose only | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~19% of this change | **1.32×** | +3.2 | 0.060 | 10/39 (NCI-H460, SHP-77, …) | top dose only | position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **1.33×** | +3.2 | 0.070 | 7/43 (RPMI-7951, LoVo, …) | rises with dose | position effect removed |
| [[Decitabine (drug)]] 0.5 µM |  | **1.31×** | +3.2 | 0.070 | 5/43 (A498, A-172, …) | inconsistent across doses | position effect removed |
| [[Lenalidomide (hemihydrate) (drug)]] 5 µM |  | **1.21×** | +3.1 | 0.075 | 6/46 (SW 900, A498, …) | top dose only | position effect removed |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.44×** | +3.0 | 0.092 | 5/24 (A498, LOX-IMVI, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9928.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Pyridoxine (drug)]] 0.5 µM in 1 line (CFPAC-1 0.0891×); [[Arbutin (drug)]] 0.05 µM in 1 line (KATO III 0.0856×); [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM in 1 line (A549 0.0988×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **0.826×** | -7.8 | 4e-12 | 29/48 (PANC-1, HEC-1-A, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 5 µM |  | 0.825× | -3.2 | 0.40 | 7/48 (RKO, PANC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9928. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 5.62 | 0 | 1 | — | [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM 0.0988× (z -9.3) |
| [[CFPAC-1 (line)]] | alt | 5.35 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.0891× (z -10.1) |
| [[KATO III (line)]] | alt | 5.89 | 0 | 1 | — | [[Arbutin (drug)]] 0.05 µM 0.0856× (z -10.1) |
| [[SHP-77 (line)]] | alt | 6.18 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.05 µM 0.0883× (z -8.6) |
| [[A-172 (line)]] | wt | 5.65 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.90 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.99 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.92 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.13 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.22 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.42 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.13 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.16 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.81 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.71 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.63 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.01 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.88 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.34 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.81 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.05 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.66 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.06 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.14 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.86 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.50 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.14 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.21 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.84 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.88 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.49 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.45 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.60 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.48 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.73 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.92 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.94 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.72 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.92 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.49 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.60 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.71 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.84 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.22 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.85 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.73 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.61 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9928), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HSPA2-AS1]] | +0.82 | +0.74 / +0.82 | both halves | 7e-06 |  |
| [[CHMP3-AS1]] | +0.82 | +0.71 / +0.78 | both halves | 7e-06 |  |
| [[LRRC37A16P]] | +0.82 | +0.67 / +0.84 | both halves | 7e-06 |  |
| [[C12orf40]] | +0.82 | +0.75 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[FLJ40194]] | +0.81 | +0.65 / +0.82 | both halves | 7e-06 |  |
| [[C2CD5-AS1]] | +0.81 | +0.72 / +0.80 | both halves | 7e-06 |  |
| [[SYNM-AS1]] | +0.81 | +0.73 / +0.76 | both halves | 7e-06 |  |
| [[TICAM2-AS1]] | +0.80 | +0.66 / +0.83 | both halves | 7e-06 |  |
| [[EOGT-DT]] | +0.80 | +0.65 / +0.82 | both halves | 7e-06 |  |
| [[GEMIN7-AS1]] | +0.78 | +0.65 / +0.80 | both halves | 7e-06 |  |
| [[CTDSPL2-DT]] | +0.78 | +0.67 / +0.80 | both halves | 7e-06 |  |
| [[ZRANB2-AS1]] | +0.78 | +0.67 / +0.79 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.860). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.0, 27.3); signed map (33.6, 4.6). **Vector** length 37.2, 3.41% of its response variance represented; |z| ≥ 3 in 803 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.3 | +10.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.4 | +11.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.2 | +11.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.4 | +8.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +2.6 | +3.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.3 | +3.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.3 | +1.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.2 | +0.4 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.0 | +2.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.0 | +1.1 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.9 | -7.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | +0.3 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.4 | -1.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.4 | -0.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | -1.3 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -0.9 | -2.4 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.9 | -2.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -0.8 | -2.9 |
|  | [[Budesonide (drug)]] 5 µM |  | -0.8 | -1.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | -0.8 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | cyclic nucleotide gated channel subunit beta 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q21.3 — chr8:86,553,977-86,743,675 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously ACHM3, ACHM1, RMCH |
| Gene groups (HGNC) | Cyclic nucleotide gated channels |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NQW8](https://www.uniprot.org/uniprotkb/Q9NQW8) (Cyclic nucleotide-gated channel beta-3):

> Pore-forming subunit of the cone cyclic nucleotide-gated channel. Mediates cone photoresponses at bright light converting transient changes in intracellular cGMP levels into electrical signals. In the dark, cGMP levels are high and keep the channel open enabling a steady inward current carried by Na(+) and Ca(2+) ions that leads to membrane depolarization and neurotransmitter release from synaptic terminals. Upon photon absorption cGMP levels decline leading to channel closure and membrane …

**Summary**, from NCBI Gene [54714](https://www.ncbi.nlm.nih.gov/gene/54714):

> This gene encodes the beta subunit of a cyclic nucleotide-gated ion channel. The encoded beta subunit appears to play a role in modulation of channel function in cone photoreceptors. This heterotetrameric channel is necessary for sensory transduction, and mutations in this gene have been associated with achromatopsia 3, progressive cone dystrophy, and juvenile macular degeneration, also known as Stargardt Disease. [provided by RefSeq, Feb 2010]

**Accessions** — [HGNC:2153](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2153) · Entrez [54714](https://www.ncbi.nlm.nih.gov/gene/54714) · UniProt [Q9NQW8](https://www.uniprot.org/uniprotkb/Q9NQW8) · Ensembl [ENSG00000170289](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170289)

## Data

Gene col 9928: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9928); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9928, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9928]; `tensor/DDL_lfc|DDL_z.npy` [9928]; `embed/gene_vectors.npy` [9928]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9928 or target_col == 9928). Every well: [[CNGB3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CNGB3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
