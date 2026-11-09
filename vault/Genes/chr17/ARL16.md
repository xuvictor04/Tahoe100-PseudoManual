---
symbol: "ARL16"
type: "gene"
col: 13171
ensembl_id: "ENSG00000214087"
name: "ARF like GTPase 16"
location: "17q25.3"
module: 7
arm: "+"
pooled_cpm: 8.73
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 0
n_dd_up_clean: 7
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# ARL16

*ARF like GTPase 16* — 17q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.67× (z +11.1, q 7e-26, up in 15 of 16 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.88× (z +10.5, q 2e-23, up in 34 of 43 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Pimozide (drug)]] 0.05 µM in 1 line (AsPC-1 0.0829×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RIC8A]] (+0.65, fdr 1e-05), [[PHF5A]] (+0.64, fdr 1e-05), [[HGS]] (+0.64, fdr 1e-05, ⚠ same locus), [[COMMD5]] (+0.63, fdr 1e-05); moves opposite to [[PRPF4B]] (-0.50, fdr 4e-04), [[PPFIBP2]] (-0.50, fdr 6e-05), [[CD83]] (-0.48, fdr 6e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 13 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13171.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **2.67×** | +11.1 | 7e-26 | 15/16 (KATO III, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **2.46×** | +10.6 | 1e-23 | 27/31 (KATO III, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.88×** | +10.5 | 2e-23 | 34/43 (HS-578T, HOP62, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.01×** | +8.2 | 3e-14 | 33/45 (SW480, HT-29, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.95×** | +7.9 | 4e-13 | 33/47 (SW480, LoVo, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.92×** | +7.7 | 1e-12 | 37/47 (SW480, AsPC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.77×** | +6.7 | 2e-09 | 31/47 (SW480, A-172, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **1.75×** | +5.9 | 2e-07 | 18/26 (A-172, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.62×** | +5.4 | 5e-06 | 23/44 (NCI-H2030, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.52×** | +4.9 | 5e-05 | 23/46 (HT-29, SW 900, …) | two highest doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.54×** | +4.9 | 5e-05 | 15/43 (HS-578T, HOP62, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.45×** | +4.2 | 0.001 | 16/37 (CFPAC-1, SW480, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.28×** | +4.1 | 0.001 | 15/48 (HS-578T, NCI-H2030, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.35×** | +3.6 | 0.014 | 9/46 (NCI-H2030, SW480, …) | two highest doses | cell-cycle shift (explains ~20% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.37×** | +3.6 | 0.014 | 13/43 (SW480, NCI-H2030, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.33×** | +3.3 | 0.029 | 16/47 (HOP62, NCI-H2030, …) | two highest doses | cell-cycle shift (explains ~3% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13171.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Pimozide (drug)]] 0.05 µM in 1 line (AsPC-1 0.0829×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.752× | -3.4 | 0.45 | 6/48 (PANC-1, A-427, …) | rises with dose |  |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | 0.769× | -3.1 | 0.45 | 13/40 (A549, RPMI-7951, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | 0.833× | -3.0 | 0.45 | 8/47 (KATO III, NCI-H1573, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.36 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13171. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 13.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.68× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[AsPC-1 (line)]] | alt | 4.78 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.0829× (z -9.3) |
| [[A-172 (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.92 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.56 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.35 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.94 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.15 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.54 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.10 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.95 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.34 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.80 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.72 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.85 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.48 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.02 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.71 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.43 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.62 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.79 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.85 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.65 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.42 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.08 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.05 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.42 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.80 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.87 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.28 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.50 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.67 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.68 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.51 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.93 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.33 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.94 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.55 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 8.84 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13171), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 3 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RIC8A]] | +0.65 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[PHF5A]] | +0.64 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[HGS]] | +0.64 | +0.64 / +0.50 | both halves | 1e-05 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[COMMD5]] | +0.63 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[GTF3C5]] | +0.61 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[WDR83]] | +0.61 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[PEX16]] | +0.60 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[ZFAND2A]] | +0.60 | +0.45 / +0.64 | both halves | 3e-05 |  |
| [[VPS9D1]] | +0.59 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[TBP]] | +0.59 | +0.61 / +0.49 | both halves | 1e-05 |  |
| [[TANGO2]] | +0.58 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[KCTD5]] | +0.57 | +0.42 / +0.54 | both halves | 4e-05 |  |
| [[PCYT1A]] | +0.56 | +0.49 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRPF4B]] | -0.50 | -0.24 / -0.52 | both halves | 4e-04 |  |
| [[PPFIBP2]] | -0.50 | -0.38 / -0.43 | both halves | 6e-05 |  |
| [[CD83]] | -0.48 | -0.38 / -0.50 | both halves | 6e-05 |  |
| [[PEG10]] | -0.48 | -0.43 / -0.43 | both halves | 3e-05 |  |
| [[PPP1CC]] | -0.47 | -0.40 / -0.55 | both halves | 5e-05 |  |
| [[ABLIM1]] | -0.47 | -0.42 / -0.43 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ARL16's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.411). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-44.9, -1.5); signed map (-24.6, 0.6). **Vector** length 43.0, 5.05% of its response variance represented; |z| ≥ 3 in 777 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +4.2 | +8.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +3.0 | +3.3 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +2.8 | +5.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.8 | +4.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.7 | +10.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.3 | +4.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.1 | +0.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.1 | +2.0 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.1 | -2.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.6 | -2.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -1.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.2 | -1.5 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -0.9 | -3.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.8 | -2.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | -0.7 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | ARF like GTPase 16 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.3 — chr17:81,681,187-81,683,797 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | ARF GTPase family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q0P5N6](https://www.uniprot.org/uniprotkb/Q0P5N6) (ADP-ribosylation factor-like protein 16):

> Required for the trafficking of ciliary proteins IFT140 and INPP5E from the Golgi to the cilia, thus playing a role in ciliogenesis (By similarity). Suppresses the RNA sensing activity of RIGI in a GTP-dependent manner.

**Summary**, from NCBI Gene [339231](https://www.ncbi.nlm.nih.gov/gene/339231):

> The protein encoded by this gene belongs to the ARL (ADP-ribosylation factor-like) family of proteins, which are structurally related to ADP-ribosylation factors (ARFs). This protein has been shown to have an inhibitory role in the cellular antiviral response. This gene product interacts with the C-terminal domain of the DEXD/H-box helicase 58 (DDX58) gene product. This interaction was found to suppress the association between the DDX58 gene product and RNA, thereby negatively regulating the …

**Accessions** — [HGNC:27902](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27902) · Entrez [339231](https://www.ncbi.nlm.nih.gov/gene/339231) · UniProt [Q0P5N6](https://www.uniprot.org/uniprotkb/Q0P5N6) · Ensembl [ENSG00000214087](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000214087)

## Data

Gene col 13171: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13171); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13171, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13171]; `tensor/DDL_lfc|DDL_z.npy` [13171]; `embed/gene_vectors.npy` [13171]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13171 or target_col == 13171). Every well: [[ARL16 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARL16.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
