---
symbol: "ARFRP1"
type: "gene"
col: 2103
ensembl_id: "ENSG00000101246"
name: "ARF related protein 1"
location: "20q13.33"
module: 96
arm: "+"
pooled_cpm: 10.42
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 8
n_dd_up_clean: 6
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/096"]
generated_by: "tahoemap"
---

# ARFRP1

*ARF related protein 1* — 20q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 1.62× (z +5.7, q 8e-06, up in 13 of 28 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[9-ING-41 (drug)]] 0.5 µM: 1.58× (z +4.2, q 0.008, up in 11 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.611× (z -8.9, q 3e-16, down in 33 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAAP100]] (+0.80, fdr 7e-06), [[TAF1C]] (+0.73, fdr 7e-06), [[RHOT2]] (+0.70, fdr 7e-06); moves opposite to [[SOS1]] (-0.54, fdr 2e-05), [[NSD3]] (-0.54, fdr 1e-05), [[HIGD2A]] (-0.51, fdr 5e-05).
> It is in [[Module 096]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2103.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.62×** | +5.7 | 8e-06 | 13/28 (NCI-H2030, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.58×** | +4.2 | 0.008 | 11/43 (J82, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.38×** | +3.8 | 0.025 | 11/43 (HS-578T, A-172, …) | all doses, flat | low cells (technical?); position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.35×** | +3.7 | 0.025 | 14/44 (LoVo, LOX-IMVI, …) | top dose only | position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.35×** | +3.7 | 0.025 | 11/45 (A498, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.33×** | +3.6 | 0.026 | 15/46 (A-172, HS-578T, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.32×** | +3.4 | 0.057 | 5/43 (NCI-H23, C32, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.31×** | +3.4 | 0.057 | 7/19 (HS-578T, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | 1.33× | +3.1 | 0.10 | 9/46 (A498, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2103.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.611×** | -8.9 | 3e-16 | 33/43 (MIA PaCa-2, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.741×** | -3.8 | 0.035 | 12/48 (HS-578T, NCI-H1573, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.750×** | -3.7 | 0.035 | 12/47 (RKO, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~14% here); composition shift |
| [[Loperamide (hydrochloride) (drug)]] 5 µM |  | **0.751×** | -3.7 | 0.035 | 16/47 (NCI-H661, RKO, …) | rises with dose | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.764×** | -3.4 | 0.066 | 16/43 (HOP62, SNU-1, …) | rises with dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **0.764×** | -3.3 | 0.087 | 16/45 (RPMI-7951, H4, …) | top dose only | position effect removed |
| [[Vandetanib (drug)]] 5 µM |  | **0.776×** | -3.2 | 0.093 | 10/47 (C-33 A, C32, …) | top dose only | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.778×** | -3.2 | 0.093 | 10/48 (SW 1271, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Bosentan (hydrate) (drug)]] 0.5 µM |  | 0.760× | -3.0 | 0.15 | 7/47 (RKO, HT-29, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2103. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SK-MEL-2 (line)]] | alt | 8.73 | 0 | 2 | — | [[Cobimetinib (drug)]] 5 µM 0.0746× (z -10.3) |
| [[COLO 205 (line)]] | alt | 10.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.147× (z -9.8) |
| [[Hs 766T (line)]] | wt | 23.7 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.242× (z -11.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[hTERT-HPNE (line)]] | wt | 8.39 | 0 | 1 | — | [[Oxaprozin (drug)]] 0.05 µM 0.0816× (z -9.0) |
| [[LOX-IMVI (line)]] | wt | 6.46 | 0 | 1 | — | [[TAK-901 (drug)]] 0.05 µM 0.0516× (z -12.0) |
| [[MIA PaCa-2 (line)]] | alt | 8.00 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.158× (z -11.5) |
| [[SHP-77 (line)]] | alt | 13.7 | 0 | 1 | — | [[Brivudine (drug)]] 0.5 µM 0.0406× (z -10.3) |
| [[A-172 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 7.29 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 9.81 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.67 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.86 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.93 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.76 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.96 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.35 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.41 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.83 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.84 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.37 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.23 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.37 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.38 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.52 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.86 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.47 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.16 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.76 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 9.54 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2103), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 5 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAAP100]] | +0.80 | +0.75 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[TAF1C]] | +0.73 | +0.73 / +0.69 | both halves | 7e-06 |  |
| [[RHOT2]] | +0.70 | +0.68 / +0.67 | both halves | 7e-06 |  |
| [[ARHGDIA]] | +0.69 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[TRMT61A]] | +0.66 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[NCDN]] | +0.65 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[C15orf39]] | +0.65 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[PLEKHG4]] | +0.65 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[LZTR1]] | +0.64 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[GLI4]] | +0.64 | +0.58 / +0.60 | both halves | 8e-06 |  |
| [[THOP1]] | +0.64 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[ASB6]] | +0.63 | +0.63 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SOS1]] | -0.54 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[NSD3]] | -0.54 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[HIGD2A]] | -0.51 | -0.40 / -0.44 | both halves | 5e-05 |  |
| [[TESK2]] | -0.50 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[COX8A]] | -0.50 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[GLCCI1]] | -0.50 | -0.40 / -0.55 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 096]]; 48 genes; every member is in the + arm (projection on the module's main direction 0.701). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-11.8, -25.1); signed map (-8.7, -31.8). **Vector** length 72.0, 12.2% of its response variance represented; |z| ≥ 3 in 806 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +3.8 | +3.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.5 | +3.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.3 | +3.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.1 | +3.6 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +3.1 | +2.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.7 | +2.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.3 | +3.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.3 | +3.8 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.0 | -8.9 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -2.0 | -3.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | -1.9 | -3.2 |
|  | [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | -1.8 | +0.3 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.8 | -2.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.8 | -2.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.8 | -1.5 |
|  | [[Sulfatinib (drug)]] 5 µM |  | -1.8 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | ARF related protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.33 — chr20:63,698,642-63,708,025 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ARP, Arp1, ARL18 |
| Gene groups (HGNC) | ARF GTPase family |
| Reactome | 4 pathways, smallest: Retrograde transport at the Trans-Golgi-Network; Intra-Golgi and retrograde Golgi-to-ER traffic; Membrane Trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13795](https://www.uniprot.org/uniprotkb/Q13795) (ADP-ribosylation factor-related protein 1):

> Trans-Golgi-associated GTPase that regulates protein sorting. Controls the targeting of ARL1 and its effector to the trans-Golgi. Required for the lipidation of chylomicrons in the intestine and required for VLDL lipidation in the liver.

**Summary**, from NCBI Gene [10139](https://www.ncbi.nlm.nih.gov/gene/10139):

> The protein encoded by this gene is a membrane-associated GTP-ase which localizes to the plasma membrane and is related to the ADP-ribosylation factor (ARF) and ARF-like (ARL) proteins. This gene plays a role in membrane trafficking between the trans-Golgi network and endosomes. Alternatively spliced transcript variants encoding different isoforms have been identified. [provided by RefSeq, May 2012]

**Accessions** — [HGNC:662](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:662) · Entrez [10139](https://www.ncbi.nlm.nih.gov/gene/10139) · UniProt [Q13795](https://www.uniprot.org/uniprotkb/Q13795) · Ensembl [ENSG00000101246](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101246)

## Data

Gene col 2103: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2103); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2103, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2103]; `tensor/DDL_lfc|DDL_z.npy` [2103]; `embed/gene_vectors.npy` [2103]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2103 or target_col == 2103). Every well: [[ARFRP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARFRP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
