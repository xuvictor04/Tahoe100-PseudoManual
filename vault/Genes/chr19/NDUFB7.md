---
symbol: "NDUFB7"
type: "gene"
col: 1810
ensembl_id: "ENSG00000099795"
name: "NADH:ubiquinone oxidoreductase subunit B7"
location: "19p13.12"
module: 178
arm: "+"
pooled_cpm: 13.58
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 2
n_dd_up_clean: 3
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/178"]
generated_by: "tahoemap"
---

# NDUFB7

*NADH:ubiquinone oxidoreductase subunit B7* — 19p13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.61× (z +8.5, q 2e-14, up in 32 of 37 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.34× (z +4.1, q 0.004, up in 22 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.529× (z -8.8, q 5e-16, down in 39 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (LoVo 0.234×, NCI-H460 0.377×); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (A-427 0.169×, LoVo 0.202×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.237×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SDHB]] (+0.73, fdr 7e-06), [[SNX4]] (+0.72, fdr 7e-06), [[NDUFB6]] (+0.71, fdr 7e-06); moves opposite to [[DDX5]] (-0.62, fdr 2e-05), [[AGO2]] (-0.57, fdr 2e-05).
> It is in [[Module 178]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1810.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.61×** | +8.5 | 2e-14 | 32/37 (NCI-H460, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.39×** | +8.3 | 4e-14 | 26/28 (PANC-1, LoVo, …) | all doses, flat | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.24×** | +7.4 | 3e-11 | 23/31 (HEC-1-A, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~13% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.72×** | +5.1 | 4e-05 | 25/40 (SW480, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~26% of this change | **1.66×** | +5.0 | 6e-05 | 26/44 (HOP62, NCI-H2030, …) | inconsistent across doses | low cells (technical?) |
| [[Selinexor (drug)]] 5 µM |  | **1.34×** | +4.1 | 0.004 | 22/48 (KATO III, NCI-H2347, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Radotinib (drug)]] 5 µM |  | **1.31×** | +3.8 | 0.012 | 20/48 (PANC-1, SHP-77, …) | top dose only | position effect removed |
| [[Infigratinib (drug)]] 0.05 µM |  | **1.41×** | +3.2 | 0.087 | 14/48 (Hs 766T, NCI-H460, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1810.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (LoVo 0.234×, NCI-H460 0.377×); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (A-427 0.169×, LoVo 0.202×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.237×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.529×** | -8.8 | 5e-16 | 39/47 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.601×** | -5.0 | 2e-04 | 26/46 (A-427, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1810. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 13.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.234× (z -11.4) |
| [[A-427 (line)]] | wt | 18.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.169× (z -9.4) |
| [[NCI-H460 (line)]] | wt | 9.90 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.377× (z -8.7) |
| [[RKO (line)]] | wt | 11.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.237× (z -9.1) |
| [[SNU-1 (line)]] | wt | 11.4 | 0 | 1 | — | [[Regorafenib (drug)]] 0.05 µM 0.0696× (z -9.0) |
| [[A-172 (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.77 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.71 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.36 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.08 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.85 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.29 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.64 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.35 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 13.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1810), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SDHB]] | +0.73 | +0.74 / +0.59 | both halves | 7e-06 | pathway: HALLMARK_ADIPOGENESIS; STRING 865 |
| [[SNX4]] | +0.72 | +0.67 / +0.65 | both halves | 7e-06 |  |
| [[NDUFB6]] | +0.71 | +0.61 / +0.67 | both halves | 7e-06 | same gene group; pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 999 |
| [[TENT2]] | +0.71 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[MED23]] | +0.69 | +0.61 / +0.69 | both halves | 7e-06 |  |
| [[CDK5RAP1]] | +0.69 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[NDUFS5]] | +0.69 | +0.63 / +0.63 | both halves | 7e-06 | same gene group; pathway: Aerobic respiration and respiratory electron transport; STRING 999 |
| [[COX16]] | +0.69 | +0.60 / +0.69 | both halves | 7e-06 | pathway: Aerobic respiration and respiratory electron transport |
| [[ASB7]] | +0.68 | +0.71 / +0.66 | both halves | 7e-06 |  |
| [[LRIG2]] | +0.68 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[EYA3]] | +0.68 | +0.59 / +0.68 | both halves | 7e-06 |  |
| [[KLHDC10]] | +0.67 | +0.64 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DDX5]] | -0.62 | -0.47 / -0.63 | both halves | 2e-05 |  |
| [[AGO2]] | -0.57 | -0.52 / -0.49 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 178]]; 22 genes; every member is in the + arm (projection on the module's main direction 0.805). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-3.3, -12.0); signed map (-32.8, -11.0). **Vector** length 54.6, 9.55% of its response variance represented; |z| ≥ 3 in 560 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +4.5 | +4.1 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +4.1 | +2.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.0 | +0.8 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.5 | +1.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.0 | +5.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.0 | +1.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.8 | +3.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +2.2 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.5 | +2.2 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -3.2 | -8.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.6 | -5.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -1.8 | -2.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.4 | -2.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.2 | -1.9 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.9 | -2.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | -0.9 | -0.8 |
|  | [[Hydroxyurea (drug)]] 5 µM |  | -0.9 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | NADH:ubiquinone oxidoreductase subunit B7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.12 — chr19:14,566,078-14,572,066 (-) |
| Ensembl biotype | protein_coding |
| Also known as | B18, CI-B18, MGC2480 |
| Gene groups (HGNC) | NADH:ubiquinone oxidoreductase supernumerary subunits |
| Hallmark sets | ADIPOGENESIS, OXIDATIVE_PHOSPHORYLATION |
| Reactome | 3 pathways, smallest: Complex I biogenesis; Respiratory electron transport; Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [P17568](https://www.uniprot.org/uniprotkb/P17568) (NADH dehydrogenase):

> Accessory subunit of the mitochondrial membrane respiratory chain NADH dehydrogenase (Complex I), that is believed not to be involved in catalysis. Complex I functions in the transfer of electrons from NADH to the respiratory chain. The immediate electron acceptor for the enzyme is believed to be ubiquinone.

**Summary**, from NCBI Gene [4713](https://www.ncbi.nlm.nih.gov/gene/4713):

> The protein encoded by this gene is a subunit of the multisubunit NADH:ubiquinone oxidoreductase (complex I). Mammalian complex I is composed of 45 different subunits. It is located at the mitochondrial inner membrane. This protein has NADH dehydrogenase activity and oxidoreductase activity. It transfers electrons from NADH to the respiratory chain. The immediate electron acceptor for the enzyme is believed to be ubiquinone. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:7702](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7702) · Entrez [4713](https://www.ncbi.nlm.nih.gov/gene/4713) · UniProt [P17568](https://www.uniprot.org/uniprotkb/P17568) · Ensembl [ENSG00000099795](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000099795)

## Data

Gene col 1810: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1810); `tables/drug_effects.parquet` (10 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1810, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1810]; `tensor/DDL_lfc|DDL_z.npy` [1810]; `embed/gene_vectors.npy` [1810]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1810 or target_col == 1810). Every well: [[NDUFB7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NDUFB7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
