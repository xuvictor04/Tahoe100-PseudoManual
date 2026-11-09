---
symbol: "AMDHD1"
type: "gene"
col: 6295
ensembl_id: "ENSG00000139344"
name: "amidohydrolase domain containing 1"
location: "12q23.1"
module: 19
arm: "+"
pooled_cpm: 2.06
n_lines_expressing: 39
n_dd_up: 34
n_dd_down: 0
n_dd_up_clean: 23
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# AMDHD1

*amidohydrolase domain containing 1* — 12q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 34 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.88× (z +11.3, q 9e-27, up in 0 of 1 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.61× (z +10.0, q 3e-21, up in 9 of 16 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H460 0.130×); [[c-Kit-IN-1 (drug)]] 0.05 µM in 1 line (NCI-H460 0.120×; ⚠ unreliable plate only); [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM in 1 line (NCI-H2347 0.0561×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SERPINB11]] (+0.66, fdr 1e-05), [[KCNK2]] (+0.65, fdr 9e-06), [[NCKAP5-AS2]] (+0.63, fdr 7e-06).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 11 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 34 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6295.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.88×** | +11.3 | 9e-27 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.61×** | +10.0 | 3e-21 | 9/16 (NCI-H2030, A-172, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.72×** | +9.7 | 5e-20 | 2/5 (SW480, NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.28×** | +8.6 | 1e-15 | 17/28 (SW480, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.34×** | +8.2 | 2e-14 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **2.07×** | +7.6 | 3e-12 | 9/28 (NCI-H460, Panc 03.27, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~11% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.63×** | +6.9 | 5e-10 | 0/4 | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.87×** | +6.5 | 4e-09 | 9/29 (J82, SHP-77, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.25×** | +6.0 | 2e-07 | 11/18 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **2.16×** | +5.7 | 7e-07 | 15/33 (NCI-H460, H4, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.19×** | +5.6 | 1e-06 | 4/13 (SW480, LoVo, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.00×** | +5.1 | 1e-05 | 9/31 (NCI-H1573, HOP62, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.00×** | +5.1 | 1e-05 | 3/27 (A498, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM |  | **1.84×** | +4.5 | 3e-04 | 11/20 (NCI-H460, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.54×** | +4.5 | 3e-04 | 1/18 (SW480) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM |  | **1.74×** | +4.1 | 0.002 | 4/18 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Amsacrine (drug)]] 5 µM |  | **1.44×** | +3.8 | 0.006 | 5/26 (A-427, NCI-H23, …) | top dose only |  |
| [[Saquinavir (drug)]] 5 µM |  | **1.43×** | +3.7 | 0.006 | 2/14 (SW480, A498) | inconsistent across doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.62×** | +3.6 | 0.011 | 2/31 (NCI-H460, CFPAC-1) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6295.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H460 0.130×); [[c-Kit-IN-1 (drug)]] 0.05 µM in 1 line (NCI-H460 0.120×; ⚠ unreliable plate only); [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM in 1 line (NCI-H2347 0.0561×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 0.669× | -3.0 | 0.92 | 5/30 (Hs 766T, A-427, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.38 per unit of S-phase module lfc, -0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6295. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 20.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.130× (z -13.7) |
| [[NCI-H2347 (line)]] | alt | 1.71 | 0 | 1 | — | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM 0.0561× (z -8.5) |
| [[A-172 (line)]] | wt | 0.814 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.61 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.950 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.64 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.546 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.767 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.457 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.269 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.584 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.641 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.02 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.333 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.84 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.817 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.560 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.308 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.653 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.394 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.824 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.263 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.14 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.523 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.804 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.352 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.850 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.328 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.763 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.490 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.44 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.465 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.904 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.86 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.515 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.675 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.44 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6295), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SERPINB11]] | +0.66 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[KCNK2]] | +0.65 | +0.64 / +0.57 | both halves | 9e-06 |  |
| [[NCKAP5-AS2]] | +0.63 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[SLITRK4]] | +0.63 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[SPDYE10]] | +0.63 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[NXPH1]] | +0.62 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[GLP2R]] | +0.60 | +0.62 / +0.46 | both halves | 2e-05 |  |
| [[RHOH]] | +0.60 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[PLAC4]] | +0.59 | +0.52 / +0.44 | both halves | 3e-05 |  |
| [[LINC00461]] | +0.59 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[DPP10]] | +0.59 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[LIN7A]] | +0.58 | +0.59 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers AMDHD1's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 6.2% of all compounds | 0.007 | ⚠ off-target possible; 5 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.673). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (46.1, 36.5); signed map (43.1, 45.3). **Vector** length 36.6, 5.72% of its response variance represented; |z| ≥ 3 in 676 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.0 | +11.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.0 | +8.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.7 | +9.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.4 | +8.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.2 | +6.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.3 | +6.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +1.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.2 | +5.7 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.1 | +2.9 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.1 | -0.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.0 | +0.1 |
|  | [[Belinostat (drug)]] 5 µM |  | -1.0 | +5.1 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.0 | -1.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.9 | -0.9 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -0.9 | -1.3 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -0.9 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | amidohydrolase domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q23.1 — chr12:95,943,331-95,968,720 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC35366 |
| Gene groups (HGNC) | M38 metallopeptidases |
| Reactome | 2 pathways, smallest: Histidine catabolism; Metabolism of amino acids and derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96NU7](https://www.uniprot.org/uniprotkb/Q96NU7) (Probable imidazolonepropionase):

> Catalyzes the hydrolytic cleavage of the carbon-nitrogen bond in imidazolone-5-propanoate to form N-formimidoyl-L-glutamate. This reaction represents the third step of the universal histidine degradation pathway. In addition to its metabolic role, functions as a tumor suppressor by promoting TGF-beta signaling. Mechanistically, inhibits ubiquitination and proteasomal degradation of SMAD4, thereby stabilizing the protein. Enhances SMAD2/3 phosphorylation and increases TGF-beta-dependent …

**Summary**, from NCBI Gene [144193](https://www.ncbi.nlm.nih.gov/gene/144193):

> Predicted to enable imidazolonepropionase activity. Predicted to be involved in L-histidine catabolic process. Predicted to be located in cytosol. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28577](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28577) · Entrez [144193](https://www.ncbi.nlm.nih.gov/gene/144193) · UniProt [Q96NU7](https://www.uniprot.org/uniprotkb/Q96NU7) · Ensembl [ENSG00000139344](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000139344)

## Data

Gene col 6295: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6295); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6295, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6295]; `tensor/DDL_lfc|DDL_z.npy` [6295]; `embed/gene_vectors.npy` [6295]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6295 or target_col == 6295). Every well: [[AMDHD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AMDHD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
