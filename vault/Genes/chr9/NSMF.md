---
symbol: "NSMF"
type: "gene"
col: 9187
ensembl_id: "ENSG00000165802"
name: "NMDA receptor synaptonuclear signaling and neuronal migration factor"
location: "9q34.3"
module: 2
arm: "+"
pooled_cpm: 29.48
n_lines_expressing: 48
n_dd_up: 15
n_dd_down: 7
n_dd_up_clean: 10
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# NSMF

*NMDA receptor synaptonuclear signaling and neuronal migration factor* — 9q34.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.34× (z +10.0, q 9e-21, up in 39 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (none with an alert); the strongest is [[Bosentan (hydrate) (drug)]] 0.5 µM: 0.681× (z -4.5, q 0.003, down in 23 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NBEAL2]] (+0.70, fdr 7e-06), [[SBF1]] (+0.68, fdr 7e-06), [[FBRSL1]] (+0.66, fdr 1e-05).
> It sits in the **+** arm of [[Module 002]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 5 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9187.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.34×** | +10.0 | 9e-21 | 39/45 (COLO 205, RKO, …) | two highest doses | cell-cycle shift (explains ~11% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **2.10×** | +8.7 | 1e-15 | 39/46 (RKO, COLO 205, …) | two highest doses | cell-cycle shift (explains ~15% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.84×** | +7.2 | 1e-10 | 40/45 (H4, COLO 205, …) | inconsistent across doses | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.70×** | +6.2 | 8e-08 | 25/40 (SW1417, J82, …) | all doses, flat | cell-cycle shift (explains ~22% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.62×** | +5.7 | 1e-06 | 29/45 (KATO III, COLO 205, …) | rises with dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.47×** | +4.5 | 5e-04 | 22/41 (LoVo, NCI-H23, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.63×** | +4.1 | 0.003 | 23/42 (J82, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.27×** | +4.0 | 0.005 | 21/46 (AsPC-1, NCI-H460, …) | top dose only |  |
| [[Sapanisertib (drug)]] 0.05 µM |  | **1.43×** | +3.9 | 0.005 | 21/46 (PANC-1, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Doxycycline (monohydrate) (drug)]] 5 µM |  | **1.40×** | +3.8 | 0.008 | 18/45 (SNU-423, BT-474, …) | top dose only | position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.54×** | +3.6 | 0.015 | 16/43 (Hs 766T, LS 180, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.38×** | +3.6 | 0.015 | 15/43 (AsPC-1, NCI-H460, …) | top dose only | cell-cycle shift (explains ~13% here); position effect removed |
| [[Almonertinib (hydrochloride) (drug)]] 0.5 µM |  | **1.34×** | +3.4 | 0.025 | 14/45 (SW480, SK-MEL-2, …) | inconsistent across doses | position effect removed |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.50×** | +3.4 | 0.029 | 11/46 (PANC-1, SW1417, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Pemigatinib (drug)]] 0.05 µM |  | **1.34×** | +3.3 | 0.040 | 15/46 (SW480, A498, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9187.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bosentan (hydrate) (drug)]] 0.5 µM |  | **0.681×** | -4.5 | 0.003 | 23/45 (AsPC-1, RKO, …) | inconsistent across doses | position effect removed |
| [[Loperamide (hydrochloride) (drug)]] 0.5 µM |  | **0.713×** | -4.0 | 0.018 | 23/46 (SNU-423, HEC-1-A, …) | two highest doses | position effect removed |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.729×** | -3.7 | 0.033 | 13/46 (LOX-IMVI, RKO, …) | inconsistent across doses | position effect removed |
| [[Gallic acid (hydrate) (drug)]] 5 µM |  | **0.803×** | -3.7 | 0.033 | 20/46 (SNU-1, MIA PaCa-2, …) | inconsistent across doses | position effect removed |
| [[Loperamide (hydrochloride) (drug)]] 5 µM |  | **0.744×** | -3.5 | 0.053 | 14/45 (PANC-1, NCI-H460, …) | two highest doses | position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **0.742×** | -3.4 | 0.058 | 15/45 (NCI-H2030, LoVo, …) | top dose only | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.578×** | -3.4 | 0.058 | 13/46 (RKO, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9187. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 186 | 0 | 5 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.347× (z -13.3) ⚠ cell-cycle shift, explains ~21% of this change |
| [[AsPC-1 (line)]] | alt | 44.1 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.65× (z +10.1) ⚠ cell-cycle shift, explains ~21% of this change | — |
| [[C32 (line)]] | wt | 11.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0597× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[hTERT-HPNE (line)]] | wt | 13.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.0690× (z -11.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 22.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -10.9) ⚠ cell-cycle shift, explains ~32% of this change |
| [[MIA PaCa-2 (line)]] | alt | 47.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.161× (z -13.6) ⚠ cell-cycle shift, explains ~93% of this change |
| [[NCI-H460 (line)]] | wt | 15.6 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.91× (z +9.5) ⚠ cell-cycle shift, explains ~21% of this change | — |
| [[RKO (line)]] | wt | 38.4 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.35× (z +8.7) | — |
| [[RPMI-7951 (line)]] | alt | 11.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0984× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 24.3 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 28.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 26.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.35 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 25.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.15 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 29.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 23.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 51.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 49.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.87 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 9.18 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.47 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.02 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 21.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.81 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 39.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9187), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NBEAL2]] | +0.70 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[SBF1]] | +0.68 | +0.75 / +0.59 | both halves | 7e-06 |  |
| [[FBRSL1]] | +0.66 | +0.67 / +0.56 | both halves | 1e-05 | same gene group |
| [[ZDHHC8]] | +0.63 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[MAPK12]] | +0.62 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[RHOT2]] | +0.62 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[KLHL17]] | +0.61 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[OPLAH]] ⚠ | +0.61 | +0.60 / +0.63 | both halves | 7e-06 | same gene group; ⚠ in the vector space only through flagged drug-doses |
| [[ZNF598]] | +0.61 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[SH3GLB2]] | +0.60 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[CACNA1H]] | +0.60 | +0.59 / +0.47 | both halves | 2e-05 |  |
| [[PPP1R12C]] | +0.60 | +0.63 / +0.48 | both halves | 2e-05 |  |
| [[FAAP100]] | +0.60 | +0.55 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.739). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-9.1, -23.7); signed map (-27.0, 1.0). **Vector** length 87.6, 19.2% of its response variance represented; |z| ≥ 3 in 746 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +6.3 | +2.9 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +5.8 | +4.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.3 | +6.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.8 | +8.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.3 | +2.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.7 | +2.4 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +3.7 | +4.1 |
|  | [[Thymol (drug)]] 0.5 µM |  | +3.2 | +2.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.2 | +2.2 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +2.9 | +3.6 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -3.8 | -3.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~93% of this change | -3.5 | -0.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.5 | -2.4 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -2.3 | -1.8 |
|  | [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | -2.3 | -1.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.2 | -2.6 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -2.2 | -3.7 |
|  | [[Afatinib (drug)]] 0.5 µM |  | -2.2 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | NMDA receptor synaptonuclear signaling and neuronal migration factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.3 — chr9:137,447,570-137,459,334 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously NELF |
| Gene groups (HGNC) | MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6X4W1](https://www.uniprot.org/uniprotkb/Q6X4W1) (NMDA receptor synaptonuclear signaling and neuronal migration factor):

> Couples NMDA-sensitive glutamate receptor signaling to the nucleus and triggers long-lasting changes in the cytoarchitecture of dendrites and spine synapse processes. Part of the cAMP response element-binding protein (CREB) shut-off signaling pathway. Stimulates outgrowth of olfactory axons and migration of gonadotropin-releasing hormone (GnRH) and luteinizing-hormone-releasing hormone (LHRH) neuronal cells.

**Summary**, from NCBI Gene [26012](https://www.ncbi.nlm.nih.gov/gene/26012):

> The protein encoded by this gene is involved in guidance of olfactory axon projections and migration of luteinizing hormone-releasing hormone neurons. Defects in this gene are a cause of idiopathic hypogonadotropic hypogonadism (IHH). Several transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, May 2010]

**Accessions** — [HGNC:29843](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29843) · Entrez [26012](https://www.ncbi.nlm.nih.gov/gene/26012) · UniProt [Q6X4W1](https://www.uniprot.org/uniprotkb/Q6X4W1) · Ensembl [ENSG00000165802](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165802)

## Data

Gene col 9187: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9187); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9187, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9187]; `tensor/DDL_lfc|DDL_z.npy` [9187]; `embed/gene_vectors.npy` [9187]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9187 or target_col == 9187). Every well: [[NSMF — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NSMF.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
