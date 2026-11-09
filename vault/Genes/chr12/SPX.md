---
symbol: "SPX"
type: "gene"
col: 5577
ensembl_id: "ENSG00000134548"
name: "spexin hormone"
location: "12p12.1"
module: 37
arm: "+"
pooled_cpm: 3.97
n_lines_expressing: 38
n_dd_up: 17
n_dd_down: 0
n_dd_up_clean: 9
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/037"]
generated_by: "tahoemap"
---

# SPX

*spexin hormone* — 12p12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 7.06× (z +18.5, q 0e+00, up in 20 of 21 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H2030 0.225×, NCI-H460 0.270×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC02680]] (+0.74, fdr 7e-06), [[WDR49]] (+0.72, fdr 7e-06), [[EFCAB12]] (+0.71, fdr 7e-06).
> It is in [[Module 037]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[LINC00862]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 8 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5577.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **7.06×** | +18.5 | 0e+00 | 20/21 (A498, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **7.99×** | +13.4 | 3e-38 | 10/12 (NCI-H1573, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **6.13×** | +11.2 | 7e-27 | 5/7 (J82, A549, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **4.80×** | +10.1 | 9e-22 | 16/24 (HOP62, SW480, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.33×** | +9.4 | 5e-19 | 3/6 (J82, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **3.87×** | +9.0 | 2e-17 | 15/27 (HOP62, A-172, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.74×** | +8.8 | 1e-16 | 4/11 (J82, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.49×** | +8.0 | 7e-14 | 12/21 (HOP62, HS-578T, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.86×** | +5.8 | 3e-07 | 12/32 (A498, HepG2/C3A, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.68×** | +4.9 | 6e-05 | 8/31 (HOP62, NCI-H2347, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.95×** | +4.4 | 5e-04 | 2/11 (J82, A498) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.49×** | +4.4 | 6e-04 | 4/5 (A498, A549, …) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.90×** | +4.2 | 0.001 | 9/26 (A498, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.76×** | +3.6 | 0.013 | 5/13 (A498, J82, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.68×** | +3.4 | 0.021 | 4/16 (SW480, SHP-77, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.64×** | +3.3 | 0.036 | 7/29 (H4, A-172, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.65×** | +3.2 | 0.040 | 4/22 (NCI-H23, LOX-IMVI, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5577.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H2030 0.225×, NCI-H460 0.270×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Loperamide (hydrochloride) (drug)]] 0.5 µM |  | 0.628× | -3.2 | 0.59 | 6/31 (LoVo, C32, …) | inconsistent across doses |  |
| [[Infigratinib (drug)]] 0.05 µM |  | 0.620× | -3.1 | 0.59 | 5/27 (HT-29, NCI-H1573, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5577. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 4.95 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.02× (z +10.2) | — |
| [[HOP62 (line)]] | alt | 3.01 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.99× (z +8.5) | — |
| [[HS-578T (line)]] | alt | 2.27 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 17.1× (z +8.5) | — |
| [[J82 (line)]] | alt | 5.24 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.19× (z +9.1) | — |
| [[NCI-H2030 (line)]] | alt | 47.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.225× (z -14.1) |
| [[NCI-H2347 (line)]] | alt | 2.19 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.9× (z +9.3) | — |
| [[NCI-H460 (line)]] | wt | 13.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -10.2) |
| [[A-172 (line)]] | wt | 1.71 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.33 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.35 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.809 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.789 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.36 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.719 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.49 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.898 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.62 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.11 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.05 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.23 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.53 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.92 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.998 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.454 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.533 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.664 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.50 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.828 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.781 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.738 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.77 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.603 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.805 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.21 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5577), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02680]] | +0.74 | +0.70 / +0.64 | both halves | 7e-06 |  |
| [[WDR49]] | +0.72 | +0.69 / +0.64 | both halves | 7e-06 |  |
| [[EFCAB12]] | +0.71 | +0.60 / +0.68 | both halves | 7e-06 |  |
| [[CCDC62]] | +0.71 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[LDHC]] | +0.71 | +0.59 / +0.72 | both halves | 7e-06 |  |
| [[C9orf153]] | +0.70 | +0.64 / +0.58 | both halves | 8e-06 |  |
| [[CORIN]] | +0.68 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[IMPA1P1]] | +0.68 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[MIA]] | +0.68 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[PHKG1]] | +0.68 | +0.55 / +0.68 | both halves | 1e-05 |  |
| [[TEX29]] | +0.67 | +0.57 / +0.65 | both halves | 1e-05 |  |
| [[CCDC181]] | +0.67 | +0.52 / +0.68 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SPX's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00862]] | B | SPX activity raises LINC00862's level | lines that do not express SPX (12) vs lines expressing it (38) | 2.03× lower at baseline in the lines without SPX | 0.007 | ⚠ within organs, on part of the lines; also absent: SYNE1, DPYS; maybe low, not absent |

## Where it sits

- **Module**: [[Module 037]]; 123 genes; every member is in the + arm (projection on the module's main direction 0.732). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (27.7, -18.0); signed map (11.3, 6.0). **Vector** length 53.8, 9.60% of its response variance represented; |z| ≥ 3 in 781 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.1 | +18.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.2 | +9.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.2 | +11.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.6 | +8.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +5.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.4 | +9.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +4.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.8 | +2.9 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.6 | +3.3 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | -2.3 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | -0.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -0.1 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -2.4 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -1.5 | -2.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.4 | -1.4 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -1.4 | -2.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.4 | -1.9 |
|  | [[Phenylephrine (hydrochloride) (drug)]] 0.5 µM |  | -1.3 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | spexin hormone |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p12.1 — chr12:21,526,296-21,541,249 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC10946, NPQ, spexin, SPX1; previously C12orf39 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BT56](https://www.uniprot.org/uniprotkb/Q9BT56) (Spexin):

> Plays a role as a central modulator of cardiovascular and renal function and nociception. Also plays a role in energy metabolism and storage. Inhibits adrenocortical cell proliferation with minor stimulation on corticosteroid release (By similarity).; [Spexin-1]: Acts as a ligand for galanin receptors GALR2 and GALR3. Intracerebroventricular administration of the peptide induces an increase in arterial blood pressure, a decrease in both heart rate and renal excretion and delayed natriuresis. …

**Summary**, from NCBI Gene [80763](https://www.ncbi.nlm.nih.gov/gene/80763):

> The protein encoded by this gene is a hormone involved in modulation of cardiovascular and renal function. It has also been shown in rats to cause weight loss. Several transcript variants have been found for this gene. [provided by RefSeq, Feb 2016]

**Accessions** — [HGNC:28139](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28139) · Entrez [80763](https://www.ncbi.nlm.nih.gov/gene/80763) · UniProt [Q9BT56](https://www.uniprot.org/uniprotkb/Q9BT56) · Ensembl [ENSG00000134548](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134548)

## Data

Gene col 5577: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5577); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5577, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5577]; `tensor/DDL_lfc|DDL_z.npy` [5577]; `embed/gene_vectors.npy` [5577]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5577 or target_col == 5577). Every well: [[SPX — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPX.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
